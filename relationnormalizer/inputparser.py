import os

def _is_file_empty(file_path):
    return os.stat(file_path).st_size == 0

def read_file_path():
    print("Input Dataset")
    print("Enter the absolute file path to the CSV file you want to normalize:")

    file_path_input = fr"{input()}"

    if (not os.path.isfile(file_path_input)):
        raise Exception("Invalid Usage: Path to file is not found.")

    if (not file_path_input.endswith(".csv")):
        raise Exception("Invalid Usage: File provided is not a CSV file.")

    if (_is_file_empty(file_path_input)):
        raise Exception("Invalid Usage: CSV file is empty.")

    return file_path_input

def read_functional_dependencies():
    print("Successful file path input.\n")
    print("Input Functional Dependencies")
    print("Format: attribute1 -> attribute2, attribute3, ..., attributeN")
    print("Type “exit” and hit enter to complete your dependency list:")

    return ""

def read_normal_form():
    print("Input Desired Normal Form")
    print("Choose the highest normal form to reach "
            "(1NF, 2NF, 3NF, BCNF, 4NF, 5NF):")

    normal_form_input = input()

    if (normal_form_input not in ("1NF", "2NF", "3NF", "BCNF", "4NF", "5NF")):
        raise Exception("Invalid Usage: Normal form provided is not a valid option.")

    return normal_form_input