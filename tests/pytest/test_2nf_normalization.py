import sys
sys.path.append("../relational-database-normalizer/src")

from key import Key
from dependency import Dependency
from relation import Relation
from typing import List
import iohandler
import normalizer
import pytest


def test_2nf_normalization() -> None:
    file_name: str = "tests/input/employee_projects.csv"

    input_relation_primary_key: Key = Key(["Ssn", "Pnumber"])
    input_relation_candidate_keys: List[Key] = [Key(["Ssn", "Pnumber"])]
    input_relation_functional_dependencies: List[Dependency] = [
        Dependency(["Ssn", "Pnumber"], ["Hours"], False),
        Dependency(["Ssn"], ["Ename"], False),
        Dependency(["Pnumber"], ["Pname", "Plocation"], False),
    ]

    input_relation: Relation = Relation(
        iohandler.read_relation_name(file_name),
        iohandler.read_relation_attributes(file_name),
        input_relation_candidate_keys,
        input_relation_primary_key,
        input_relation_functional_dependencies,
        []
    )

    normalized_relations: List[Relation] = normalizer.normalize(input_relation, "2NF")

    assert normalized_relations[0] == Relation(
        "EMPLOYEE_PROJECTS",
        ["Ssn", "Pnumber", "Hours"],
        [Key(["Ssn", "Pnumber"])],
        Key(["Ssn", "Pnumber"]),
        [Dependency(["Ssn", "Pnumber"], ["Hours"], False)],
        []
    )

    assert normalized_relations[1] == Relation(
        "EMPLOYEE_PROJECTS_1",
        ["Ssn", "Ename"],
        [Key(["Ssn"])],
        Key(["Ssn"]),
        [Dependency(["Ssn"], ["Ename"], False)],
        []
    )

    assert normalized_relations[2] == Relation(
        "EMPLOYEE_PROJECTS_2",
        ["Pnumber", "Pname", "Plocation"],
        [Key(["Pnumber"])],
        Key(["Pnumber"]),
        [Dependency(["Pnumber"], ["Pname", "Plocation"], False)],
        []
    )
