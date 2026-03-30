import os
import argparse
from dotenv import load_dotenv
from google import genai

parser = argparse.ArgumentParser(description="A Gemini API Chatbot")
parser.add_argument("user_prompt", type=str, help="The prompt for the Chatbot to respond to.")
args = parser.parse_args()

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
else:
    print("GEMINI_API_KEY loaded successfully.")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = args.user_prompt
)

if response.usage_metadata:
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
else:
    raise RuntimeError("Usage metadata not found in response.")

print(response.text)