from typing import List


class Key:
    def __init__(self, attributes: List[str]) -> None:
        self.attributes: List[str] = attributes

    def __repr__(self) -> str:
        result: str = "("

        for attribute in self.attributes:
            is_last: bool = attribute == self.attributes[-1]
            result += f"{attribute}{", " if not is_last else ")"}"

        return result
    
    def __eq__(self, other) -> bool:
        return self.attributes == other.attributes