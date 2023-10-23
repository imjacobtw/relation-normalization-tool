from relation import Relation
import inputparser
import os
import sys

def get_relation_name(file_path):
    base = os.path.basename(file_path)
    split_base = os.path.splitext(base)
    relation_name = split_base[0]
    return relation_name.capitalize()

if __name__ == "__main__":
    relation_input = Relation()

    try:
        file_path = inputparser.read_file_path()
        print("Success: CSV file provided.\n")
        functional_dependencies = inputparser.read_functional_dependencies()
        print("Success: Functional dependencies provided.\n")
        normal_form = inputparser.read_normal_form()
        print("Success: Desired normal form provided.\n")
    except Exception as e:
        sys.exit(e)

    relation_input.name = get_relation_name(file_path)

    pass
    