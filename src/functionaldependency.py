class FunctionalDependency:
    def __init__(self):
        self.leftSide = []
        self.rightSide = []


    def IsPartial(self, relation):
        leftSideOnlyPrimeAttributes = True
        leftSideContainsEveryPrimeAttribute = True
        rightSideAllNonPrimeAttributes = True

        if (self.leftSide != relation.primaryKey.attributes):
            leftSideContainsEveryPrimeAttribute = False

        for attribute in self.leftSide:
            if (not AttributeIsPrime(relation, attribute)):
                leftSideOnlyPrimeAttributes = False

        for attribute in self.rightSide:
            if (AttributeIsPrime(relation, attribute)):
                rightSideAllNonPrimeAttributes = False

        return (leftSideOnlyPrimeAttributes) and \
               (not leftSideContainsEveryPrimeAttribute) and \
               (rightSideAllNonPrimeAttributes)
    

    
    def __repr__(self):
        return f"{self.leftSide} -> {self.rightSide}"


def AttributeIsPrime(relation, attribute):
    for key in relation.keys:
        if (attribute in key.attributes):
            return True
    return False