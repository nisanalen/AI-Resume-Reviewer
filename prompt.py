class PromptManager:
    def generate_prompt(self, about_user, field, experience_level, job_level, resume_text):
        # Prompt template for interpreting the CV based on user data
        return f"""Based on the user's description and provided information:
        - About the user: {about_user}
        - Field wants to work: {field}
        - Experience Level: {experience_level}
        - Job Level: {job_level}

        Please analyze and interpret the content of the uploaded resume below and provide insights:

        Resume Text: {resume_text}"""
