import os
MAX_CHARS = 10000


def get_files_info(working_directory, directory="."):
    root_path = os.path.abspath(".")
    actual_directory = os.path.abspath(os.path.join(root_path,working_directory))
    target_directory = os.path.abspath(os.path.join(actual_directory,directory))
    if not os.path.abspath(target_directory).startswith(actual_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'

    file_list = os.listdir(target_directory)
    print(f"Result for '{directory}' directory:")
    for file in file_list:
        file_path = os.path.join(target_directory,file)
        print(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
    
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