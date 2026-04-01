import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

parser = argparse.ArgumentParser(description="A Gemini API Chatbot")
parser.add_argument("user_prompt", type=str, help="The prompt for the Chatbot to respond to.")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output for debugging purposes.")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in environment variables.")
else:
    print("GEMINI_API_KEY loaded successfully.")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = messages
)

if response.usage_metadata:
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    else:
        print(f"Prompt tokens: {prompt_tokens}, Response tokens: {response_tokens}")
else:
    raise RuntimeError("Usage metadata not found in response.")

print(response.text)