import sys
sys.path.append("../relational-database-normalizer/src")

from key import Key
from dependency import Dependency
from relation import Relation
from typing import List
import iohandler
import normalizer
import pytest


def test_3nf_normalization() -> None:
    file_name: str = "tests/input/employee_departments.csv"

    input_relation_primary_key: Key = Key(["Ssn"])
    input_relation_candidate_keys: List[Key] = [Key(["Ssn"])]
    input_relation_functional_dependencies: List[Dependency] = [
        Dependency(["Ssn"], ["Ename", "Bdate", "Address", "Dnumber"], False),
        Dependency(["Dnumber"], ["Dname", "Dmgr_ssn"], False),
    ]

    input_relation: Relation = Relation(
        iohandler.read_relation_name(file_name),
        iohandler.read_relation_attributes(file_name),
        input_relation_candidate_keys,
        input_relation_primary_key,
        input_relation_functional_dependencies,
        []
    )

    normalized_relations: List[Relation] = normalizer.normalize(input_relation, "3NF")

    assert normalized_relations[0] == Relation(
        "EMPLOYEE_DEPARTMENTS",
        ["Ename", "Ssn", "Bdate", "Address", "Dnumber"],
        [Key(["Ssn"])],
        Key(["Ssn"]),
        [Dependency(["Ssn"], ["Ename", "Bdate", "Address", "Dnumber"], False)],
        []
    )

    assert normalized_relations[1] == Relation(
        "EMPLOYEE_DEPARTMENTS_3",
        ["Dnumber", "Dname", "Dmgr_ssn"],
        [Key(["Dnumber"])],
        Key(["Dnumber"]),
        [Dependency(["Dnumber"], ["Dname", "Dmgr_ssn"], False)],
        []
    )
