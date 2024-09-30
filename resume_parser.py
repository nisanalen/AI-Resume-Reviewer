import PyPDF2
# from docx import Document  # Uncomment if you plan to handle DOCX files

class ResumeParser:
    def parse(self, file_path, file_type):
        resume_text = ""
        if file_type == "application/pdf":
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    resume_text += page.extract_text()

        # DOCX parsing logic if needed
        # elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        #     doc = Document(file_path)
        #     resume_text = "\n".join([p.text for p in doc.paragraphs])
        
        return resume_text
