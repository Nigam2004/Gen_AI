import os
from typing import List, Optional
from pydantic import BaseModel,Field
from google import genai
from dotenv import load_dotenv
load_dotenv()

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
print(client)
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)
recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)