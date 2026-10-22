from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import Field, BaseModel
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

class Worker(BaseModel):
    name:str=Field(description="Worker's full name")
    uan: Optional[str] = Field(
        default=None,
        description="Worker's UAN"
    )
    esic_number: Optional[str] = None

llm=ChatGoogleGenerativeAI(model="gemini-3.8-flash")
llm_structured=llm.with_structured_output(Worker)
result=llm_structured.invoke("Worker name is Rahul Das. UAN is 123456789012.")
print(result.name)
print(result.uan)
print(result.esic_number)