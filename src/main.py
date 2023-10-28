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

    try:
        inputFilePath = inputparser.ReadInputFilePath()
        console.print("Successful: CSV file provided.\n", style=successStyle)

        relationInput.name = Relation.GetNameFromFile(inputFilePath)
        relationInput.attributes = Relation.GetAttributesFromFile(inputFilePath)

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

        outputFilePath = inputparser.ReadOutputFilePath()
        console.print(
            "Successful: Output file path provided.\n",
            style=successStyle
        )
    except Exception as e:
        console.print(e, style=failureStyle)
        sys.exit()

    relationInput.functionalDependencies = functionalDependencies
    relationInput.primaryKey = primaryKey
    outputFileName = relationInput.name.lower() + ".sql"

    normalizedRelations = normalizer.Normalize(relationInput, normalForm)
    querygenerator.GenerateQueryOutput(
        normalizedRelations,
        outputFilePath,
        outputFileName
    )


if __name__ == "__main__":
    Main()
