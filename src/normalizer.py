from key import Key
from relation import Relation

newRelationNumber = 1

def Normalize(relation, normalForm):
    return ConvertTo2NF(relation)

    normalizationMaps = {
        "1NF": ConvertTo1NF,
        "2NF": ConvertTo2NF,
        "3NF": ConvertTo3NF,
        "BCNF": ConvertToBCNF,
        "4NF": ConvertTo4NF,
        "5NF": ConvertTo5NF,
    }

    normalizedRelations = normalizationMaps[normalForm](relation)
    return normalizedRelations


def DetermineHighestNormalForm(relation):
    highestNormalForm = "1NF"

    if (IsIn2NF(relation)):
        highestNormalForm = "2NF"

    if (IsIn3NF(relation)):
        highestNormalForm = "3NF"

    if (IsInBCNF(relation)):
        highestNormalForm = "BCNF"

    if (IsIn4NF(relation)):
        highestNormalForm = "4NF"

    if (IsIn5NF(relation)):
        highestNormalForm = "5NF"

    return highestNormalForm


def ConvertTo1NF(relation):
    return [relation]


def ConvertTo2NF(relation):
    if (IsIn2NF(relation)):
        return [relation]
    
    global newRelationNumber
    normalizedRelations = []
    fullRelation = Relation()

    fullRelation.name = f"{relation.name}_{newRelationNumber}"
    newRelationNumber += 1
    fullRelation.primaryKey = relation.primaryKey
    fullRelation.keys = relation.keys
    fullRelation.attributes = relation.attributes
    normalizedRelations.append(fullRelation)

    for functionalDependency in relation.functionalDependencies:
        if (functionalDependency.IsPartial(relation)):
            for attribute in functionalDependency.rightSide:
                fullRelation.attributes.remove(attribute)

            partialRelation = Relation()
            partialRelation.name = f"{relation.name}_{newRelationNumber}"
            newRelationNumber += 1
            partialRelation.attributes = functionalDependency.leftSide + \
                                         functionalDependency.rightSide
            
            partialRelationKey = Key()
            partialRelationKey.attributes = functionalDependency.leftSide
            partialRelationKey.isPrimary = True

            partialRelation.primaryKey = partialRelationKey
            partialRelation.keys.append(partialRelationKey)
            partialRelation.functionalDependencies.append(functionalDependency)
            normalizedRelations.append(partialRelation)
        else:
            fullRelation.functionalDependencies.append(functionalDependency)

    return normalizedRelations


def ConvertTo3NF(relation):
    pass


def ConvertToBCNF(relation):
    pass


def ConvertTo4NF(relation):
    pass


def ConvertTo5NF(relation):
    pass


def IsIn2NF(relation):
    for functionalDependency in relation.functionalDependencies:
        if (functionalDependency.IsPartial(relation)):
            return False
    return True


def IsIn3NF(relation):
    return False


def IsInBCNF(relation):
    return False


def IsIn4NF(relation):
    return False


def IsIn5NF(relation):
    return False