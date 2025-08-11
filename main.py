import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


def main():
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    
    verbose = False
    if len(sys.argv)<2:
        print("Usage: python3 main.py <string prompt> (--verbose)")
        sys.exit(1)
    
    if len(sys.argv)==3:
        if sys.argv[2]=="--verbose":
            verbose = True

    user_prompt = sys.argv[1]

    messages = [
        types.Content(role="user",parts=[types.Part(text=user_prompt)])
    ]


    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model="gemini-2.0-flash-001",
    contents=messages,
    config = types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt))
    print("response:", response.text)
    calls = response.function_calls
    for call in calls:
        print(f"Calling function: {call.name}({call.args})")

    if verbose:
        print("User prompt:",user_prompt)
        print("Prompt tokens:",response.usage_metadata.prompt_token_count)
        print("Response tokens:",response.usage_metadata.candidates_token_count)




if __name__ == "__main__":
    main()

