from file_operations import modify_file
from exception_handling import get_filename_from_user, read_user_file

def main():
    """Main function to demonstrate file and exception handling."""
    # File Read & Write Challenge
    input_file = "data/input.txt"  # Ensure this file exists
    output_file = "data/output.txt"
    modification_result = modify_file(input_file, output_file)
    print(f"File Modification Result: {modification_result}")

    # Error Handling Lab
    user_filename = get_filename_from_user()
    file_content = read_user_file(user_filename)
    print(f"File Content:\n{file_content}")

if __name__ == "__main__":
    main()
