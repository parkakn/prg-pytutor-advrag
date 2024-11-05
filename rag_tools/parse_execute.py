import glob
from dotenv import load_dotenv
import nest_asyncio
import os
import subprocess

from rag_tools.document_parsing import documentparser

# Docx to Markdown, Pdf to Markdown using LLM

# Needed to use document_parser function 
nest_asyncio.apply()
openai_api_key = os.environ.get("OPENAI_API_KEY")
llama_cloud_api_key = os.environ.get("LLAMA_CLOUD_API_KEY")

# Converting docx to pdf file 
def convert_docx_to_pdf(docx_path,folder_b_path):
    # Convert DOCX to PDF
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', docx_path,'--outdir', folder_b_path])

# Example: 
# folder_path = "GSU/Assignments/*.pdf"
# Parsing pdf to markdown 
def pdf_to_markdown(folder_path, document_type):
    # Selects all pdf files in folder_path --> "GSU/Assignments/*.pdf" 
    files_pdf = glob.glob(folder_path)  
    # Select LLM model to to parse documents into markdown
    model_mini = "openai-gpt4o-mini"
    # Parse documents 
    md_assignments = documentparser.document_to_markdown(files_pdf,document_type,model_mini)

    for i in range(len(md_assignments)):    
        # Save to .txt file 
        txt_file_name = os.path.basename(files_pdf[i]).replace('.pdf', '.txt')
        
        # Save
        folder_name = folder_path.replace('*.pdf', '')
        with open(folder_name+f'''{txt_file_name}''', "w") as file:
            file.write(md_assignments[i][0].text)

# Example: 
# folder_path = "GSU/Assignments/*.docx"
# select document_type from: 
# "lab manual", "assignment", "in-class exercise", "lecture slide", "quizzes and exams"
# document_type = "assignment"
# This function takes path of folder containing docx files and the document type as inputs and saves text files of the documents in text files in the same folder 
def docx_to_markdown(folder_path, document_type):
    files_docx = glob.glob(folder_path)  
    folder_b_path = folder_path.replace('*.docx', '')
    for i in files_docx:
        convert_docx_to_pdf(i,folder_b_path)
        # Save docx as pdf file in the same folder 
        #print(f"Converted {i} to PDF")
        
    folder_path_pdf = folder_path.replace('.docx', '.pdf')
    pdf_to_markdown(folder_path_pdf, document_type)


