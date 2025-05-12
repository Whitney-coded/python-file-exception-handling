def read_file(filepath):
    """Reads the content of a file."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: An error occurred: {e}"

def write_file(filepath, content):
    """Writes content to a file, creating it if it doesn't exist."""
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return "File successfully written."
    except Exception as e:
        return f"Error: An error occurred: {e}"

def modify_file(input_filepath, output_filepath):
    """Reads a file, modifies content, and writes to a new file."""
    content = read_file(input_filepath)
    if "Error" in str(content):
        return content  # Return the error message

    modified_content = content.upper()  # Example modification: convert to uppercase
    write_result = write_file(output_filepath, modified_content)
    return write_result
