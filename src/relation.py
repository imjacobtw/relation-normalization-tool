from key import Key
from typing import List


class Relation:
    def __init__(
        self,
        name: str,
        attributes: List[str],
        candidate_keys: List[Key],
        primary_key: Key,
    ) -> None:
        self.name: str = name
        self.attributes: List[str] = attributes
        self.candidate_keys: List[Key] = candidate_keys
        self.primary_key: Key = primary_key


    def __repr__(self) -> None:
        result: str = f"{self.name.upper()}("

        for attribute in self.attributes:
            is_last: bool = attribute == self.attributes[-1]
            is_primary_key_attribute: bool = attribute in self.primary_key.attributes
            
            result += "*" if is_primary_key_attribute else ""
            result += attribute.name
            result += "*" if is_primary_key_attribute else ""
            result += ", " if not is_last else ")"

        return result