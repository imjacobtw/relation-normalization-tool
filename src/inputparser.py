from functionaldependency import FunctionalDependency
from key import Key
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


def IsValidFunctionalDependency(functionalDependency, attributes):
    allAttributes = functionalDependency.leftSide + functionalDependency.rightSide
    
    for attribute in allAttributes:
        if (attribute not in attributes):
            return False

    return True


def ReadFunctionalDependencies(attributes):
    print("Please provide the functional dependencies of the relation (type "
          "\"exit\" when finished):")
    print("Format: attribute1 -> attribute2 ... attributeN")

    userInput = input()
    functionalDependencies = []

    while (userInput != "exit"):
        functionalDependency = ParseFunctionalDependency(userInput)

        if (not IsValidFunctionalDependency(functionalDependency, attributes)):
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


def IsValidKey(key, relationAttributes):
    for attribute in key.attributes:
        if (attribute not in relationAttributes):
            return False

    return True


def ReadKeys(attributes):
    print("Please provide all of the candidate keys (type "
          "\"exit\" when finished):")
    print("Format: attribute1 ... attributeN")

    userInput = input()
    keys = []

    while (userInput != "exit"):
        key = Key()
        key.attributes = userInput.split()

        if (not IsValidKey(key, attributes)):
            raise Exception("Key contains invalid attributes.")

        keys.append(key)
        userInput = input()

    return keys


def ReadPrimaryKey(relation):
    print("Please provide the primary key of the relation:")
    print("Format: attribute1 ... attributeN")

    primaryKeyInput = input()
    splitPrimaryKeyInput = primaryKeyInput.split() 

    for key in relation.keys:
        if (splitPrimaryKeyInput == key.attributes):
            return splitPrimaryKeyInput
        
    raise Exception("Primary key input is not a key of the given relation.")
