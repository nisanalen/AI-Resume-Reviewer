# llm.py
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

class LLMHandler:
    def __init__(self):
        self.llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"))
    
    def interpret(self, about_user, field, experience_level, job_level, resume_text):
        # Generate prompt using the PromptManager class
        prompt = self.generate_prompt(about_user, field, experience_level, job_level, resume_text)

        # Set up the LLMChain with a prompt
        llm_chain = LLMChain(
            prompt=PromptTemplate(
                input_variables=["about_user", "field", "experience_level", "job_level", "resume_text"],
                template=prompt
            ),
            llm=self.llm
        )
        
        # Generate response from the LLM
        return llm_chain.run({
            "about_user": about_user,
            "field": field,
            "experience_level": experience_level,
            "job_level": job_level,
            "resume_text": resume_text
        })

    def generate_prompt(self, about_user, field, experience_level, job_level, resume_text):
        # Prompt template for interpreting the CV based on user data
        return f"""Based on the user's description and provided information:
        - About the user: {about_user}
        - Field wants to work: {field}
        - Experience Level: {experience_level}
        - Job Level: {job_level}

        Please analyze and interpret the content of the uploaded resume below and provide insights:

        Resume Text: {resume_text}"""
