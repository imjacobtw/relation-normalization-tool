from dependency import Dependency
from key import Key
from rich.console import Console
from relation import Relation
from typing import Callable, Dict, List
import copy
import iohandler


console: Console = Console()
new_relation_number: int = 1

def normalize(relation: Relation, normal_form: str) -> List[Relation]:
    print("Beginning normalization process...\n")

    normalization_maps: Dict[str, Callable] = {
        "UNF": convert_to_unf,
        "1NF": convert_to_1nf,
        "2NF": convert_to_2nf,
        "3NF": convert_to_3nf,
        # "EKNF": convert_to_eknf,
        "BCNF": convert_to_bcnf,
        # "4NF": convert_to_4nf,
        # "ETNF": convert_to_etnf,
        # "5NF": convert_to_5nf,
        # "DKNF": convert_to_dknf,
        # "6NF": convert_to_6nf,
    }

    normalized_relations: List[Relation] = normalization_maps[normal_form]([relation])
    return normalized_relations


def convert_to_unf(relations: List[Relation]) -> List[Relation]:
    console.print("UNF selected. No normalization needed.")
    return relations


def convert_to_1nf(relations: List[Relation]) -> List[Relation]:
    console.print("1NF selected. CSVs are already in 1NF.")
    return relations


def is_in_2nf(relation: Relation) -> bool:
    for functional_dependency in relation.functional_dependencies:
        if is_partial_dependency(functional_dependency, relation):
            return False
        
    return True


def convert_to_2nf(relations: List[Relation]) -> List[Relation]:
    normalized_relations: List[Relation] = relations[:]

    for relation in relations:
        print(f"Converting {relation.name} to 2NF...")

        if is_in_2nf(relation):
            print(f"  {relation.name} is already in 2NF.")
            continue

        global new_relation_number
        remove_functional_dependencies: List[Dependency] = []
        remove_attributes: List[str] = []

        for functional_dependency in relation.functional_dependencies:
            if not is_partial_dependency(functional_dependency, relation):
                continue

            print(f"  Dependency that violates 2NF: ({functional_dependency})")
            remove_functional_dependencies.append(functional_dependency)
            remove_attributes += functional_dependency.right_side

            new_relation_name: str = f"{relation.name}_{new_relation_number}"
            new_relation_number += 1
            new_relation_attributes: List[str] = functional_dependency.left_side + \
                                                 functional_dependency.right_side
            new_relation_partial_key: Key = Key(functional_dependency.left_side)
            new_relation_candidate_keys: List[Key] = [new_relation_partial_key]
            new_relation_primary_key: Key = new_relation_partial_key
            new_relation_functional_dependencies: List[Dependency] = [functional_dependency]
            new_relation_multivalued_dependencies: List[Dependency] = []

            print(f"\tCreating relation {new_relation_name}...", end="")

            normalized_relations.append(Relation(
                new_relation_name,
                new_relation_attributes,
                new_relation_candidate_keys,
                new_relation_primary_key,
                new_relation_functional_dependencies,
                new_relation_multivalued_dependencies
            ))

        print()

        for partial_functional_dependency in remove_functional_dependencies:
            relation.functional_dependencies.remove(partial_functional_dependency)
        remove_attributes_from_relation(relation, remove_attributes)

    iohandler.print_status_message(f"2NF conversion completed.\n", "success")

    return normalized_relations


def is_in_3nf(relation: Relation) -> bool:
    for functional_dependency in relation.functional_dependencies:
        if is_3nf_dependency(functional_dependency, relation):
            return False

    return is_in_2nf(relation)


def is_partial_dependency(dependency: Dependency, relation: Relation) -> bool:
    left_side_only_prime_attributes: bool = True
    left_side_contains_every_prime_attribute: bool = False
    right_side_all_nonprime_attributes: bool = True

    for key in relation.candidate_keys:
        if key.attributes == dependency.left_side:
            left_side_contains_every_prime_attribute = True

    for attribute in dependency.left_side:
        if not is_prime_attribute(relation, attribute):
            left_side_only_prime_attributes = False

    for attribute in dependency.right_side:
        if is_prime_attribute(relation, attribute):
            right_side_all_nonprime_attributes = False

    return (
        left_side_only_prime_attributes
        and (not left_side_contains_every_prime_attribute)
        and right_side_all_nonprime_attributes
    )

    
def is_prime_attribute(relation: Relation, attribute: str) -> bool:
    for key in relation.candidate_keys:
        if attribute in key.attributes:
            return True
        
    return False


def remove_attributes_from_relation(relation: Relation, attributes: List[str]) -> None:
    for attribute in attributes:
        if attribute in relation.attributes:
            relation.attributes.remove(attribute)

        for functional_dependency in relation.functional_dependencies:
            if attribute in functional_dependency.left_side:
                functional_dependency.left_side.remove(attribute)

            if attribute in functional_dependency.right_side:
                functional_dependency.right_side.remove(attribute)


def convert_to_3nf(relations: List[Relation]) -> List[Relation]:
    relations = convert_to_2nf(relations)
    normalized_relations: List[Relation] = relations[:]

    for relation in relations:
        print(f"Converting {relation.name} to 3NF...")

        if is_in_3nf(relation):
            print(f"  {relation.name} is already in 3NF.")
            continue

        global new_relation_number
        remove_functional_dependencies: List[Dependency] = []
        remove_attributes: List[str] = []

        for functional_dependency in relation.functional_dependencies:
            if not is_3nf_dependency(functional_dependency, relation):
                continue

            print(f"  Dependency that violates 3NF: ({functional_dependency})")
            remove_functional_dependencies.append(functional_dependency)
            remove_attributes += functional_dependency.right_side

            new_relation_name: str = f"{relation.name}_{new_relation_number}"
            new_relation_number += 1
            new_relation_attributes: List[str] = functional_dependency.left_side + \
                                                 functional_dependency.right_side
            new_relation_primary_key: Key = Key(functional_dependency.left_side)
            new_relation_candidate_keys: List[Key] = [new_relation_primary_key]
            new_relation_functional_dependencies: List[Dependency] = [functional_dependency]
            new_relation_multivalued_dependencies: List[Dependency] = []

            print(f"\tCreating relation {new_relation_name}...", end="")

            normalized_relations.append(Relation(
                new_relation_name,
                new_relation_attributes,
                new_relation_candidate_keys,
                new_relation_primary_key,
                new_relation_functional_dependencies,
                new_relation_multivalued_dependencies
            ))

        print()

        for partial_functional_dependency in remove_functional_dependencies:
            relation.functional_dependencies.remove(partial_functional_dependency)
        remove_attributes_from_relation(relation, remove_attributes)

    iohandler.print_status_message(f"3NF conversion completed.\n", "success")

    return normalized_relations


def is_3nf_dependency(dependency: Dependency, relation: Relation) -> bool:
    left_side_is_superkey: bool = False
    right_side_contains_only_prime_attributes: bool = True

    for key in relation.candidate_keys:
        if set(key.attributes).issubset(set(dependency.left_side)):
            left_side_is_superkey = True

    for attribute in dependency.right_side:
        if not is_prime_attribute(relation, attribute):
            right_side_contains_only_prime_attributes = False

    return not (left_side_is_superkey or right_side_contains_only_prime_attributes)


def is_in_bcnf(relation: Relation) -> bool:
    for functional_dependency in relation.functional_dependencies:
        if is_bcnf_dependency(functional_dependency, relation):
            return False

    return is_in_3nf(relation)


def is_bcnf_dependency(dependency: Dependency, relation: Relation) -> bool:
    left_side_is_superkey: bool = False

    for key in relation.candidate_keys:
        if set(key.attributes).issubset(set(dependency.left_side)):
            left_side_is_superkey = True

    return not (left_side_is_superkey)


def convert_to_bcnf(relations: List[Relation]) -> List[Relation]:
    relations = convert_to_3nf(relations)
    normalized_relations: List[Relation] = relations[:]

    for relation in relations:
        print(f"Converting {relation.name} to BCNF...")

        if is_in_bcnf(relation):
            print(f"  {relation.name} is already in BCNF.")
            continue

        global new_relation_number
        remove_functional_dependencies: List[Dependency] = []
        remove_attributes: List[str] = []

        for functional_dependency in relation.functional_dependencies:
            if not is_bcnf_dependency(functional_dependency, relation):
                continue

            print(f"  Dependency that violates BCNF: ({functional_dependency})")
            remove_functional_dependencies.append(functional_dependency)
            remove_attributes += functional_dependency.right_side

            new_relation_name: str = f"{relation.name}_{new_relation_number}"
            new_relation_number += 1
            new_relation_attributes: List[str] = functional_dependency.left_side + \
                                                 functional_dependency.right_side
            new_relation_primary_key: Key = Key(functional_dependency.left_side)
            new_relation_candidate_keys: List[Key] = [new_relation_primary_key]
            new_relation_functional_dependencies: List[Dependency] = [functional_dependency]
            new_relation_multivalued_dependencies: List[Dependency] = []

            print(f"\tCreating relation {new_relation_name}...\n", end="")

            normalized_relations.append(Relation(
                new_relation_name,
                new_relation_attributes,
                new_relation_candidate_keys,
                new_relation_primary_key,
                new_relation_functional_dependencies,
                new_relation_multivalued_dependencies
            ))

        print()

        for partial_functional_dependency in remove_functional_dependencies:
            relation.functional_dependencies.remove(partial_functional_dependency)
        remove_attributes_from_relation(relation, remove_attributes)

    iohandler.print_status_message(f"BCNF conversion completed.", "success")

    return normalized_relations


def is_in_4nf(relation: Relation) -> bool:
    return len(relation.multivalued_dependencies) == 0


def convert_to_4nf(relations: List[Relation]) -> List[Relation]:
    relations = convert_to_bcnf(relations)
    normalized_relations: List[Relation] = relations[:]

    for relation in relations:
        if len(relation.multivalued_dependencies) == 0:
            continue

        for multivalued_dependency in relation.multivalued_dependencies:
            pass

    return normalized_relations