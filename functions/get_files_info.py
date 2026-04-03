import os


def get_files_info(working_directory, directory="."):
    """Return info for files in a directory, ensuring directory is within working_directory."""
    try:
        abs_working_directory = os.path.abspath(working_directory)

        if not os.path.isdir(abs_working_directory):
            return f'Error: "{working_directory}" is not a directory'

        target_dir = os.path.normpath(os.path.join(abs_working_directory, directory))

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # Ensure the requested directory is inside working_directory
        if os.path.commonpath([abs_working_directory, target_dir]) != abs_working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Iterate over items in the target directory
        files_info = []
        for item in os.listdir(target_dir):
            full_path = os.path.join(target_dir, item)
            try:
                size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                files_info.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
            except OSError as e:
                files_info.append(f"- {item}: Error getting info: {e}")

        return "\n".join(files_info)


    except Exception as e:
        return f"Error: {e}"
    