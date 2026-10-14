import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize the Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Create a chat session object which manages the message history locally
chat = client.chats.create(model="gemini-3.8-flash")

while True:
  prompt = input("You: ").strip()

  if prompt == "0":
    break

  # Send the message to the chat session (it automatically appends and sends history)
  response = chat.send_message(prompt)

  print("Bot:", response.text)

  # If you want to inspect or print the raw local conversation history:
  print(chat.get_history())