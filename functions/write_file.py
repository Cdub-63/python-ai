import os

def write_file(working_directory, file_path, content):
    """Write content to a file, ensuring file_path is within working_directory."""
    try:
        abs_working_directory = os.path.abspath(working_directory)

        if not os.path.isdir(abs_working_directory):
            message = f'Error: "{working_directory}" is not a directory'
            print(message)
            return False

        target_file = os.path.normpath(os.path.join(abs_working_directory, file_path))

        # Ensure the requested file is inside working_directory
        if os.path.commonpath([abs_working_directory, target_file]) != abs_working_directory:
            message = f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            print(message)
            return False

        # Create parent directories if they don't exist
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, 'w') as f:
            f.write(content)

        message = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        print(message)
        return True

    except Exception as e:
        message = f"Error: {e}"
        print(message)
        return False
