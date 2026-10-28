from pypdf import PdfReader
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai  import GoogleGenerativeAIEmbeddings
from pathlib import Path
load_dotenv()
# uv run RAG_Langchain_Project/index.py

#import path
docs_dir=Path("RAG_Langchain_Project/docs")
# print(docs_dir)
DB_DIR="RAG_Langchain_Project/chroma.db"

##load documents
documents=[]
for pdf_paths in docs_dir.glob("*.pdf"):
    reader=PdfReader(str(pdf_paths))
    print(pdf_paths.name)
    # print(reader.metadata)
   
    for page_number,page in enumerate(reader.pages):
        text=page.extract_text()
        # print(page_number)
        if text.strip():
            # print(page_number)
            documents.append( Document(
            page_content=text,
            metadata={
                "sources":pdf_paths.name,
                "page_number":page_number
            }
        )
            )

# print(documents)

if not documents:
    raise ValueError("no pdfs found")
print(f"loded{len(documents)} ")

#split pdfs 
spliter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks=spliter.split_documents(documents)
# print(chunks)
print(len(chunks))

##create embeding fun
embeding=GoogleGenerativeAIEmbeddings(
    model='gemini-embedding-001'
)

##crete vector store using chroma DB
vector_store=Chroma(
    collection_name="pdf_docs",
    embedding_function=embeding,
    persist_directory=DB_DIR
)

# add chunks to the vector DB
vector_store.add_documents(chunks)

# print(chunks_chroma_db)


