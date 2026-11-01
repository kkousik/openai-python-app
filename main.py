import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Add it to the project .env file."
    )

client = genai.Client(api_key=api_key)
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

print(f"Calling {model}...", flush=True)
response = client.models.generate_content(
    model=model,
    contents="Hi, can you tell me a joke about programming?",
)
print(response.text)
