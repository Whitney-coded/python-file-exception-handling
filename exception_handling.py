def get_filename_from_user():
    """Asks the user for a filename and handles potential errors."""
    filename = input("Enter the filename: ")
    return filename

def read_user_file(filename):
    """Reads a file specified by the user, handling errors."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"
