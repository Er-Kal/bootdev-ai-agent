import os
import subprocess
from google.genai import types

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
        commands = ["python", abs_file_path]
        # Append arguments if provided
        if args:
            commands.extend(args)

        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=actual_directory, # Set the working directory for the subprocess
        )

        output_lines = []
        if result.stdout:
            output_lines.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output_lines.append(f"STDERR:\n{result.stderr}")

        # Report non-zero exit codes
        if result.returncode != 0:
            output_lines.append(f"Process exited with code {result.returncode}")

        # Return concatenated output or a "No output" message
        return "\n".join(output_lines) if output_lines else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Return the output of a python file when executed in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath of the file to execute."
            )
        }
    )
)