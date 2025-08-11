import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory,file_path):
    root_path = os.path.abspath(".")
    actual_directory = os.path.abspath(os.path.join(root_path,working_directory))
    abs_file_path = os.path.join(actual_directory, file_path)
    if not os.path.abspath(abs_file_path).startswith(actual_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(abs_file_path,"r") as f:
        file_content_string = f.read(MAX_CHARS)
        if f.read(1)!="":
            file_content_string+=f'[...File "{file_path}" truncated at 10000 characters]'
    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Return the content of a file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file that is being accessed."
            )
        }
    )
)