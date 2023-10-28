from relation import Relation
from rich.console import Console
import inputparser
import normalizer
import querygenerator
import sys


def Main():
    console = Console()
    successStyle = "bold green"
    failureStyle = "bold red"
    relationInput = Relation()
    outputFilePath = ""

    try:
        filePath = inputparser.ReadFilePath()
        console.print("Successful: CSV file provided.\n", style=successStyle)

        relationInput.name = Relation.GetNameFromFile(filePath)
        relationInput.attributes = Relation.GetAttributesFromFile(filePath)

        functionalDependencies = inputparser.ReadFunctionalDependencies(
            relationInput
        )
        console.print(
            "Successful: Functional dependencies provided.\n",
            style=successStyle
        )

        normalForm = inputparser.ReadNormalForm()
        console.print("Successful: Normal form provided.\n", style=successStyle)

        primaryKey = inputparser.ReadPrimaryKey(relationInput)
        console.print("Successful: Primary key provided.\n", style=successStyle)
    except Exception as e:
        console.print(e, style=failureStyle)
        sys.exit()

    relationInput.functionalDependencies = functionalDependencies
    relationInput.primaryKey = primaryKey

    print(relationInput.name)
    print(relationInput.attributes)
    print(relationInput.functionalDependencies)
    print(relationInput.primaryKey)

    normalizedRelations = normalizer.Normalize(relationInput, normalForm)
    querygenerator.GenerateQueryOutput(normalizedRelations, outputFilePath)


if __name__ == "__main__":
    Main()
