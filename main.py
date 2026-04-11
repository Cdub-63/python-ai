import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from config import MODEL
from call_function import available_functions, call_function

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

for iteration in range(20):
    response = client.models.generate_content(
        model=MODEL,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if response.usage_metadata:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
    else:
        raise RuntimeError("Usage metadata not found in response.")

    function_responses = []
    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)
            if not function_call_result.parts:
                raise RuntimeError("Function call result has no parts")

            function_response = function_call_result.parts[0].function_response
            if function_response is None:
                raise RuntimeError("Function response is missing from function call result")

            if function_response.response is None:
                raise RuntimeError("Function response payload is missing")

            function_responses.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_response.response}")

        if function_responses:
            messages.append(types.Content(role="user", parts=function_responses))

        continue

    print("Final response:")
    print(response.text)
    break
else:
    print("Maximum iterations reached without a final response.")
    sys.exit(1)