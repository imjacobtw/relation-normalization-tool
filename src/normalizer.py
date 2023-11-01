from key import Key
from relation import Relation
import functionaldependency

newRelationNumber = 1


def Normalize(relation, normalForm):
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
    normalForms = ("2NF", "3NF", "BCNF", "4NF", "5NF")
    normalFormFunctions = (IsIn2NF, IsIn3NF, IsInBCNF, IsIn4NF, IsIn5NF)

    for index, function in enumerate(normalFormFunctions):
        if function(relation):
            highestNormalForm = normalForms[index]

    return highestNormalForm


def ConvertTo1NF(relation):
    return [relation]


def ConvertTo2NF(relation):
    if IsIn2NF(relation):
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
        if functionalDependency.IsPartial(relation):
            for attribute in functionalDependency.rightSide:
                fullRelation.attributes.remove(attribute)

            partialRelation = Relation()
            partialRelation.name = f"{relation.name}_{newRelationNumber}"
            newRelationNumber += 1
            partialRelation.attributes = (
                functionalDependency.leftSide + functionalDependency.rightSide
            )

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
    if IsIn3NF(relation):
        return [relation]

    global newRelationNumber
    denormalizedRelations = [relation]
    normalizedRelations = []

    if not IsIn2NF(relation):
        denormalizedRelations = ConvertTo2NF(relation)

    for denormalizedRelation in denormalizedRelations:
        if IsIn3NF(denormalizedRelation):
            normalizedRelations.append(denormalizedRelation)
            continue

        parentRelation = Relation()
        parentRelation.name = f"{relation.name}_{newRelationNumber}"
        newRelationNumber += 1
        parentRelation.primaryKey = denormalizedRelation.primaryKey
        parentRelation.keys = denormalizedRelation.keys
        parentRelation.attributes = denormalizedRelation.attributes
        normalizedRelations.append(parentRelation)

        for functionalDependency in denormalizedRelation.functionalDependencies:
            leftSideIsNonkey = not LeftHandSideIsPrimeAttribute(
                functionalDependency, denormalizedRelation
            )
            rightSideIsNonkey = not RightHandSideIsPrimeAttribute(
                functionalDependency, denormalizedRelation
            )

            if leftSideIsNonkey and rightSideIsNonkey:
                for attribute in functionalDependency.rightSide:
                    parentRelation.attributes.remove(attribute)
                childRelation = Relation()
                childRelation.name = f"{relation.name}_{newRelationNumber}"
                newRelationNumber += 1
                childRelation.attributes = (
                    functionalDependency.leftSide + functionalDependency.rightSide
                )

                childRelationKey = Key()
                childRelationKey.attributes = functionalDependency.leftSide
                childRelationKey.isPrimary = True

                childRelation.primaryKey = childRelationKey
                childRelation.keys.append(childRelationKey)
                childRelation.functionalDependencies.append(functionalDependency)
                normalizedRelations.append(childRelation)
            else:
                parentRelation.functionalDependencies.append(functionalDependency)

    return normalizedRelations


def ConvertToBCNF(relation):
    return [relation]


def ConvertTo4NF(relation):
    return [relation]


def ConvertTo5NF(relation):
    return [relation]


def IsIn2NF(relation):
    for functionalDependency in relation.functionalDependencies:
        if functionalDependency.IsPartial(relation):
            return False
    return True


def IsIn3NF(relation):
    for functionalDependency in relation.functionalDependencies:
        if not (
            LeftHandSideIsPrimeAttribute(functionalDependency, relation)
            or RightHandSideIsPrimeAttribute(functionalDependency, relation)
        ):
            return False
    return IsIn2NF(relation)


def LeftHandSideIsPrimeAttribute(functionalDependency, relation):
    for attribute in functionalDependency.leftSide:
        if functionaldependency.AttributeIsPrime(relation, attribute):
            return True
    return False


def RightHandSideIsPrimeAttribute(functionalDependency, relation):
    for attribute in functionalDependency.rightSide:
        if functionaldependency.AttributeIsPrime(relation, attribute):
            return True
    return False


def IsInBCNF(relation):
    for functionalDependency in relation.functionalDependencies:
        if not LeftHandSideIsPrimeAttribute(functionalDependency, relation):
            return False
    return IsIn3NF(relation)


def IsIn4NF(relation):
    return False


def IsIn5NF(relation):
    return False
