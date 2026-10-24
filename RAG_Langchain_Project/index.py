from pypdf import PdfReader
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai  import ChatGoogleGenerativeAI
from pathlib import Path
load_dotenv()

#import path
docs_dir=Path("RAG_Langchain_Project/docs")
print(docs_dir)
DB_DIR="./chroma.db"
##load documents

documents=[]
for pdf_paths in docs_dir.glob("*.pdf"):
    reader=PdfReader(str(pdf_paths))
    print(pdf_paths.name)
    print(reader.metadata)
   

    for page_number,page in enumerate(reader.pages):
       text=page.extract_text()
    #    print(text)
    if text.strip():
        documents.extend( Document(
            page_content=text,
            metadata={
                "sources":pdf_paths.name,
                "page_number":page_number
            }
        )
            )
    print(documents)

    if not documents:
        raise ValueError("no pdfs found")
    print(f"loded{len(documents)} ")



