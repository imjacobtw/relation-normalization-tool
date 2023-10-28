from functionaldependency import FunctionalDependency
import os


def FileIsEmpty(filePath):
    return os.stat(filePath).st_size == 0


def ReadInputFilePath():
    print("Please provide the absolute path to the CSV file with the relation"
          " you want to normalize:")

    filePathInput = fr"{input()}"

    if (not os.path.exists(filePathInput)):
        raise Exception("Path to file is invalid.")
    
    if (not filePathInput.endswith(".csv")):
        raise Exception("File is not a CSV file.")
    
    if (FileIsEmpty(filePathInput)):
        raise Exception("File is empty.")

    return filePathInput


def ReadOutputFilePath():
    print("Please provide the absolute path to the directory for the output:")

    filePathInput = fr"{input()}"
    
    if (not os.path.isdir(filePathInput)):
        raise Exception("Path provided is not a valid directory.")

    return filePathInput


def ParseFunctionalDependency(userInput):
    functionalDependency = FunctionalDependency()
    splitUserInput = userInput.split()
    arrowIndex = splitUserInput.index("->")

    for i in range(0, arrowIndex):
        attribute = splitUserInput[i]
        functionalDependency.leftSide.append(attribute)

    for i in range(arrowIndex + 1, len(splitUserInput)):
        attribute = splitUserInput[i]
        functionalDependency.rightSide.append(attribute)

    return functionalDependency


def IsValidFunctionalDependency(functionalDependency, relation):
    for attribute in functionalDependency.leftSide:
        if (attribute not in relation.attributes):
            return False
        
    for attribute in functionalDependency.rightSide:
        if (attribute not in relation.attributes):
            return False

    return True


def ReadFunctionalDependencies(relation):
    print("Please provide the functional dependencies of the relation (type "
          "\"exit\" when finished):")
    print("Format: attribute1 -> attribute2 ... attributeN")

    userInput = input()
    functionalDependencies = []

    while (userInput != "exit"):
        functionalDependency = ParseFunctionalDependency(userInput)

        if (not IsValidFunctionalDependency(functionalDependency, relation)):
            raise Exception("Functional dependency contains invalid attributes.")

        functionalDependencies.append(functionalDependency)
        userInput = input()

    return functionalDependencies


def ReadNormalForm():
    print("Please provide the normal form you want to the relation to be in "
          "(1NF, 2NF, 3NF, BCNF, 4NF, 5NF):")

    normalFormInput = input()

    if (normalFormInput not in ("1NF", "2NF", "3NF", "BCNF", "4NF", "5NF")):
        raise Exception("Unknown normal form provided.")

    return normalFormInput


def ReadPrimaryKey(relation):
    print("Please provide the primary/composite key of the relation:")
    print("Format: attribute1 ... attributeN")

    primaryKeyInput = input()
    splitPrimaryKeyInput = primaryKeyInput.split()

    for attribute in splitPrimaryKeyInput:
        if (attribute not in relation.attributes):
            raise Exception(f"Attribute \"{attribute}\" is not an attribute " +
                            f"of the given relation \"{relation.name}\".")
        
    return splitPrimaryKeyInput

