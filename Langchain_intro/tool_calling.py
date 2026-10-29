from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
@tool
def  check_worker(uan:str)->str :
    """check where the uan exist or not """
    if uan=="1234567890":
        return "uan number already exist"
    return "new worker"

tools={
    "check_worker":check_worker
}

llm=ChatGoogleGenerativeAI(model="gemini-3.8-flash")
llm_with_tools=llm.bind_tools([check_worker])
response=llm_with_tools.invoke("Check whether worker UAN 1234567890 already exists")

for tool_call in response.tool_calls:
    tool_name=tool_call["name"]
    tool_args=tool_call["args"]
    print(type(tool_call))
    res=tools[tool_name].invoke(tool_args)
    print(res)


