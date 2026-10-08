import os
from typing import List, Optional
from pydantic import BaseModel,Field
from google import genai
from dotenv import load_dotenv
load_dotenv()
## chat bot
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

while True:
    prompt=input("You:")
    if prompt=="0":
        break
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
    )
    print("Bot:",interaction.output_text)
