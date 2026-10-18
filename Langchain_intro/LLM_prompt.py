from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a worker-document assistant."),
    ("human", "Extract the worker's name from this text: {text}")
])

messages = prompt.invoke({
    "text": "Worker name is Rahul Das"
})

print(messages)