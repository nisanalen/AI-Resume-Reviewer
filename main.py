# main.py
import streamlit as st
from resume_parser import ResumeParser
from db import SQLDatabaseHandler  # Update to use SQLDatabaseHandler
from llm import LLMHandler
from prompt import PromptManager
import tempfile

# Initialize the required components
resume_parser = ResumeParser()
data_store = SQLDatabaseHandler()  # Change to SQLDatabaseHandler
llm_handler = LLMHandler()
prompt_manager = PromptManager()

# Streamlit Interface
st.title("Welcome to the CV Review Portal with AI Assistance")

# Large Input Section - User talks about themselves
st.subheader("Tell us about yourself")
about_user = st.text_area("Introduce yourself here", height=200)

# Field Menu
st.subheader("Field you want to work")
field = st.selectbox("Select your field:", 
                    ["Data Science", "AI Engineering", "Business Development", "Management Consulting", "Marketing"])

# Experience Open Menu
st.subheader("Experience Level")
experience_level = st.selectbox("Select your experience level:", 
                                ["Internship", "Entry Level", "Mid Level", "Senior Level", "Executive"])

# Job Level Open Menu
st.subheader("Job Position")
job_level = st.selectbox("Select the job position you are applying for:", 
                         ["Intern", "Junior", "Mid", "Senior", "Lead", "Manager"])

# Resume Upload Section
st.subheader("Upload your resume")
uploaded_resume = st.file_uploader("Choose a file", type=["pdf", "docx"])

# Submit Button
if st.button("Submit"):
    if uploaded_resume is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_resume.read())
            file_path = tmp_file.name

        # Parse resume using the ResumeParser class
        resume_text = resume_parser.parse(file_path, uploaded_resume.type)

        # Save user data in SQL database using SQLDatabaseHandler class
        data_store.add_texts(about_user, field, experience_level, job_level)

        # Generate prompt using the PromptManager class
        prompt = prompt_manager.generate_prompt(about_user, field, experience_level, job_level, resume_text)

        # Get the AI interpretation of the resume using LLMHandler class
        result = llm_handler.interpret(about_user, field, experience_level, job_level, resume_text)


        st.write("AI's Interpretation of your Resume:")
        st.write(result)
        
    else:
        st.error("Please upload a resume to proceed.")
