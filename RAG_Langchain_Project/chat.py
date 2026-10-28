from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
load_dotenv()

# create ambeding
embeding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
#vector db
vector_db=Chroma(
    collection_name="pdf_docs",
    embedding_function=embeding,
    persist_directory="RAG_Langchain_Project/chroma.db"
)

##call LLM
llm=ChatGoogleGenerativeAI("gemini-3.8-flash")

##create chat prompt

prompt=ChatPromptTemplate.from_template(
    """ansere the question only the context below
    
    if you are unable to found the answere in this context
    then tell that you could not find it in the documents.
    
    context:
    {context}
    question:
    {question}

    Answere:

    """
)

#ask question

while True:
    question=input("\n ask a question:")

    if question.lower()=="exit":
        break
    #retrive the 4 most siliar answere as per the questions
    docs=vector_db.similarity_search(question,k=4 )

  #context for prompt
    context="\n\n".join(
        f"sources:{doc.metadata.get("sources","uknown")}"
        f"page:{doc.metadata.get("page","uknown")}\n"
        for doc in docs
    )

    message=prompt.invoke(
        {"context":context,
         "question":question}
        )
    response=llm.invoke(message)

    print(response.content)

   



