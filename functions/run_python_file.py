import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_directory = os.path.abspath(working_directory)

        if not os.path.isdir(abs_working_directory):
            return f'Error: "{working_directory}" is not a directory'

        target_file = os.path.normpath(os.path.join(abs_working_directory, file_path))

        # Ensure the requested file is inside working_directory
        if os.path.commonpath([abs_working_directory, target_file]) != abs_working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=abs_working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )

        output_parts = []
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
        else:
            if result.stdout:
                output_parts.append(f"STDOUT: {result.stdout}")
            if result.stderr:
                output_parts.append(f"STDERR: {result.stderr}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"

        