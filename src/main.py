from dependency import Dependency
from key import Key
from relation import Relation
from typing import List
import iohandler
import normalizer
import sqlgenerator
import sys


def main(args: List[str]) -> None:
    try:
        input_file_path: str = iohandler.read_input_file_path()
        iohandler.print_status_message("CSV file provided.", "success")

        relation_name: str = iohandler.read_relation_name(input_file_path)
        iohandler.print_status_message("Relation name parsed.", "success")
        relation_attributes: List[str] = iohandler.read_relation_attributes(input_file_path)
        iohandler.print_status_message("Attributes parsed.\n", "success")

        relation_candidate_keys: List[Key] = iohandler.read_candidate_keys(relation_attributes)
        iohandler.print_status_message("Candidate keys provided.\n", "success")

        relation_primary_key: Key = iohandler.read_primary_key(relation_candidate_keys)
        iohandler.print_status_message("Primary key provided.\n", "success")

        relation_functional_dependencies: List[Dependency] = iohandler.read_dependencies(relation_attributes, False)
        iohandler.print_status_message("Functional dependencies provided.\n", "success")

        relation_multivalued_dependencies: List[Dependency] = iohandler.read_dependencies(relation_attributes, True)
        iohandler.print_status_message("Multivalued dependencies provided.\n", "success")

        normal_form: str = iohandler.read_normal_form()
        iohandler.print_status_message("Normal form provided.\n", "success")
    except Exception as e:
        iohandler.print_status_message(str(e), "failure")
        sys.exit()

    input_relation: Relation = Relation(
        relation_name,
        relation_attributes,
        relation_candidate_keys,
        relation_primary_key,
        relation_functional_dependencies,
        relation_multivalued_dependencies
    )

    iohandler.print_status_message(
        "CSV files will have heuristically generated SQL data types. It " \
        "is recommended to review the data types for the attributes " \
        "after the normalization process.",
        "notice"
    )

    iohandler.print_status_message(
        "CSV relation schemas are automatically in 1NF due to the standard of CSV files.\n",
        "notice"
    )

    try:
        normalized_relations: List[Relation] = normalizer.normalize(
            input_relation,
            normal_form
        )

        iohandler.print_status_message("Normalization process complete.\n", "success")
        print(sqlgenerator.generate_sql_statements(normalized_relations))
    except Exception as e:
        iohandler.print_status_message("There was an error normalizing the relation.", "failure")
        sys.exit()


if __name__ == "__main__":
    main(sys.argv)
