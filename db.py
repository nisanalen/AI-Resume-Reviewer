import sqlite3
from contextlib import closing

class SQLDatabaseHandler:
    def __init__(self, db_name='user_data.db'):
        # Connect to SQLite database (or create it)
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        # Create a table if it doesn't exist
        with closing(self.connection.cursor()) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    about_user TEXT,
                    field TEXT,
                    experience_level TEXT,
                    job_level TEXT
                )
            ''')
            self.connection.commit()

    def add_texts(self, about_user, field, experience_level, job_level):
        # Insert a new entry into the database
        with closing(self.connection.cursor()) as cursor:
            cursor.execute('''
                INSERT INTO user_data (about_user, field, experience_level, job_level) 
                VALUES (?, ?, ?, ?)
            ''', (about_user, field, experience_level, job_level))
            self.connection.commit()

    def close(self):
        # Close the database connection
        self.connection.close()