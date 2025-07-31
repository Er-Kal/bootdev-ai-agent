import os
import subprocess

def run_python_file(working_directory,file_path, args=[]):
    root_path = os.path.abspath(".")
    actual_directory = os.path.abspath(os.path.join(root_path,working_directory))
    abs_file_path = os.path.join(actual_directory, file_path)
    if not os.path.abspath(abs_file_path).startswith(actual_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        process = subprocess.run(["python",abs_file_path,*args],timeout=30)
        
        stdout = process.stdout
        stderr = process.stderr
        if stderr!=None:
            print(f"STDERR: {stderr}")
        if process.returncode!=0:
            print(f"Process exited with code {process.returncode}")
        return f"STDOUT: {stdout}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    