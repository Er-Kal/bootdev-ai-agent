import os

def write_file(working_directory,file_path,content):
    root_path = os.path.abspath(".")
    actual_directory = os.path.abspath(os.path.join(root_path,working_directory))
    abs_file_path = os.path.join(actual_directory, file_path)
    if not os.path.abspath(abs_file_path).startswith(actual_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(actual_directory):
        os.makedirs(actual_directory)
    
    with open(abs_file_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'