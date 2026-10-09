import os
from google import genai
from dotenv import load_dotenv
load_dotenv() 

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


## check the this api key support which emnbeding model
for model in client.models.list():
    if "embed" in model.name:
        print(model.name)


response=client.models.embed_content(
    model="gemini-embedding-001",
    contents="how are you",
)

print(response)
print(response.embeddings)
vector=response.embeddings[0].values
print(vector)

