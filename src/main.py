from key import Key
from relation import Relation
from typing import List
import iohandler
import sys


def main(args: List[str]) -> None:
    try:
        input_file_path: str = iohandler.read_input_file_path()
        iohandler.print_status_message("CSV file provided.", "success")

        relation_name: str = iohandler.read_relation_name(input_file_path)
        iohandler.print_status_message("Relation name parsed.", "success")
        relation_attributes: List[str] = iohandler.read_relation_attributes(input_file_path)
        iohandler.print_status_message("Attributes parsed.\n", "success")

        iohandler.print_status_message(
            "CSV files will have heuristically generated SQL data types. It " \
            "is recommended to review the data types for the attributes " \
            "after the normalization process.\n",
            "notice"
        )

        relation_candidate_keys: List[Key] = iohandler.read_candidate_keys(relation_attributes)
        iohandler.print_status_message("Candidate keys provided.\n", "success")

        relation_primary_key: Key = iohandler.read_primary_key(relation_candidate_keys)
        iohandler.print_status_message("Primary key provided.\n", "success")
    except Exception as e:
        iohandler.print_status_message(str(e), "failure")
        sys.exit()

    input_relation: Relation = Relation(
        relation_name,
        relation_attributes,
        relation_candidate_keys,
        relation_primary_key
    )

    print(input_relation)
if __name__ == "__main__":
    main(sys.argv)
