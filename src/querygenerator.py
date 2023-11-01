def GenerateQueryOutput(normalizedRelations, filePath):
    file = open(filePath, "w")
    
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
        "INT": ["id", "number", "no", "hours"],
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

    for key in primaryKey.attributes:
        primaryKeyString += key

        if (key != primaryKey.attributes[-1]):
            primaryKeyString += ", "

    resultString += f"{primaryKeyString})\n"
    return resultString