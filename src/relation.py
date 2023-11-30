from dependency import Dependency
from key import Key
from typing import List


class Relation:
    def __init__(
        self,
        name: str,
        attributes: List[str],
        candidate_keys: List[Key],
        primary_key: Key,
        functional_dependencies: List[Dependency],
        multivalued_dependencies: List[Dependency]
    ) -> None:
        self.name: str = name
        self.attributes: List[str] = attributes
        self.candidate_keys: List[Key] = candidate_keys
        self.primary_key: Key = primary_key
        self.functional_dependencies: List[Dependency] = functional_dependencies
        self.multivalued_dependencies: List[Dependency] = multivalued_dependencies


    def __repr__(self) -> str:
        result: str = f"{self.name.upper()}("

        for attribute in self.attributes:
            is_last: bool = attribute == self.attributes[-1]
            is_primary_key_attribute: bool = attribute in self.primary_key.attributes
            
            result += "*" if is_primary_key_attribute else ""
            result += attribute
            result += "*" if is_primary_key_attribute else ""
            result += ", " if not is_last else ")\n"

        for key in self.candidate_keys:
            result += f"{key}\n"

        for functional_dependenecy in self.functional_dependencies:
            result += f"{functional_dependenecy}\n"

        for multivalued_dependency in self.multivalued_dependencies:
            result += f"{multivalued_dependency}"

        return result
    

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Relation):
            return NotImplemented

        return (self.name == other.name) and \
               (self.attributes == other.attributes) and \
               (self.candidate_keys == other.candidate_keys) and \
               (self.primary_key == other.primary_key) and \
               (self.functional_dependencies == other.functional_dependencies) and \
               (self.multivalued_dependencies == other.multivalued_dependencies)