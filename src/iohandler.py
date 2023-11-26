from key import Key
from rich.console import Console
from rich.text import Text
from typing import Any, Dict, List, Literal
import csv
import os


def read_input_file_path() -> str:
    input_file_path: str = rf"{input(
        "Provide the path to the file with the relation(s) you want to normalize:\n"
    )}"

    if not os.path.exists(input_file_path):
        raise Exception("Provided path is invalid.")

    if not input_file_path.endswith(".csv"):
        raise Exception("File is not a CSV file.")

    if os.stat(input_file_path).st_size == 0:
        raise Exception("File is empty.")

    return input_file_path


def print_status_message(
    message_input: str, 
    status: Literal["success", "failure", "notice"]
) -> None:
    console: Console = Console()
    message: Text = Text()
    message.append(f"[{status}] {message_input}")

    message_styles: Dict[str, str] = {
        "success": "green",
        "failure": "red",
        "notice": "blue"
    }

    message.stylize(message_styles[status], 1, len(status) + 1)
    console.print(message)


def read_relation_name(file_path: str) -> str:
    return os.path.splitext(os.path.basename(file_path))[0].upper()


def read_relation_attributes(file_path: str) -> List[str]:
    with open(file_path) as file:
        csv_reader: Any = csv.reader(file)
        return next(csv_reader)


def read_candidate_keys(relation_attributes: List[str]) -> List[Key]:
    print("Provide all of the candidate keys (type \"exit\" when finished):")
    print("Format: attribute1 ... attributeN")

    user_input: str = input()
    candidate_keys: List[Key] = []

    while user_input.lower() != "exit":
        attributes: List[str] = user_input.split()
        candidate_key: Key = Key(attributes)

        if not is_valid_key(candidate_key, relation_attributes):
            raise Exception("Key contains invalid attributes.")

        candidate_keys.append(candidate_key)
        user_input = input()

    return candidate_keys


def is_valid_key(key: Key, relation_attributes: List[str]) -> bool:
    for attribute in key.attributes:
        if attribute not in relation_attributes:
            return False
        
    return True


def read_primary_key(candidate_keys: List[Key]) -> Key:
    print("Provide the primary key (type \"exit\" when finished):")
    print("Format: attribute1 ... attributeN")

    user_input: str = input()
    attributes: List[str] = user_input.split()
    primary_key: Key = Key(attributes)

    if not is_key_in_relation(primary_key, candidate_keys):
        raise Exception("Primary key is not a candidate key of the relation.")
    
    return primary_key


def is_key_in_relation(key: Key, relation_candidate_keys: List[Key]) -> bool:
    for candidate_key in relation_candidate_keys:
        if key == candidate_key:
            return True
    
    return False