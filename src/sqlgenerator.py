from key import Key
from relation import Relation
from typing import Dict, List

def generate_sql_statements(relations: List[Relation]) -> str:
    statements: str = ""

    for relation in relations:
        create_table_statement: str = generate_create_table_statement(relation)
        statements += create_table_statement

    statements = statements[:-2]
    return statements


def generate_create_table_statement(relation: Relation) -> str:
    create_table_statement: str = f"CREATE TABLE {relation.name} (\n"

    for attribute in relation.attributes:
        attribute_type: str = generate_attribute_type(attribute)
        create_table_statement += f"\t{attribute} {attribute_type},\n"

    create_table_statement += generate_primary_key_statement(relation.primary_key)
    create_table_statement += f");\n\n"
    return create_table_statement


def generate_attribute_type(attribute_name: str) -> str:
    attribute_potential_types: Dict[str, List[str]] = {
        "INT": ["id", "number", "hours", "ssn"],
        "DATE": ["start", "end", "day", "date"],
        "REAL": ["rate", "price"]
    }

    for data_type, potential_substrings in attribute_potential_types.items():
        for substring in potential_substrings:
            if substring in attribute_name.lower():
                return data_type
            
    return "VARCHAR(255)"


def generate_primary_key_statement(primary_key: Key) -> str:
    return f"\tPRIMARY KEY {primary_key}\n"