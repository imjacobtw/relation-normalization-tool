from typing import List


class Dependency:
    def __init__(self, left_side: List[str], right_side: List[str]) -> None:
        self.left_side: List[str] = left_side
        self.right_side: List[str] = right_side
        