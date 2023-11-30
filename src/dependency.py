from typing import List
import copy


class Dependency:
    def __init__(
        self,
        left_side: List[str], 
        right_side: List[str], 
        is_multivalued: bool
    ) -> None:
        self.left_side: List[str] = left_side
        self.right_side: List[str] = right_side
        self.is_multivalued = is_multivalued

    def __repr__(self) -> str:
        result: str = ""

        for attribute in self.left_side:
            result += f"{attribute} "

        result += "->>" if self.is_multivalued else "->"

        for attribute in self.right_side:
            result += f" {attribute}"

        return result
    
    def __copy__(self) -> "Dependency":
        return Dependency(self.left_side[:], self.right_side[:], self.is_multivalued)
        