import os

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