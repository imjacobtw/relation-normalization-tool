class FunctionalDependency:
    @classmethod
    def __init__(self, leftSide = [], rightSide = []):
        self.leftSide = leftSide
        self.rightSide = rightSide

    @classmethod
    def __str__(self):
        resultString = ""

        for attribute in self.leftSide:
            resultString += f"{attribute}, "

        resultString += "-> "

        for attribute in self.rightSide:
            resultString += f"{attribute}, "

        return resultString