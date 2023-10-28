import os


def GenerateQueryOutput(normalizedRelations, outputFilePath, fileName):
    fullFilePath = os.path.join(outputFilePath, fileName)
    file = open(fullFilePath, "w")
    
    for relation in normalizedRelations:
        createTableStatement = GenerateCreateTableStatement(relation)
        file.write(createTableStatement)


def GenerateCreateTableStatement(relation):
    resultString = f"CREATE TABLE {relation.name} (\n"

    for attribute in relation.attributes:
        attributeType = GenerateAttributeType(attribute)
        resultString += f"\t{attribute} {attributeType},\n"

    resultString += GeneratePrimaryKeyStatement(relation.primaryKey)
    resultString += f");\n\n"
    return resultString


def GenerateAttributeType(attributeName):
    attributePotentialTypes = {
        "INT": ["id"],
        "DATE": ["start", "end"],
    }

    for (dataType, potentialSubstrings) in attributePotentialTypes.items():
        for substring in potentialSubstrings:
            if (substring in attributeName.lower()):
                return dataType

    return "VARCHAR(255)"


def GeneratePrimaryKeyStatement(primaryKey):
    resultString = f"\tPRIMARY KEY ("
    primaryKeyString = ""

    for key in primaryKey:
        primaryKeyString += key

        if (key != primaryKey[-1]):
            primaryKeyString += ", "

    resultString += f"{primaryKeyString})\n"
    return resultString