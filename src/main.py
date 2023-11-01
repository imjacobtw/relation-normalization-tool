from relation import Relation
from rich.console import Console
import inputparser
import normalizer
import os
import querygenerator
import sys


def Main():
    console = Console()
    successStyle = "bold green"
    infoStyle = "bold deep_sky_blue1"
    failureStyle = "bold red"
    relationInput = Relation()

    try:
        inputFilePath = inputparser.ReadInputFilePath()
        console.print("Successful: CSV file provided.\n", style=successStyle)

        relationInput.name = Relation.GetNameFromFile(inputFilePath)
        relationInput.attributes = Relation.GetAttributesFromFile(inputFilePath)

        functionalDependencies = inputparser.ReadFunctionalDependencies(
            relationInput.attributes
        )
        console.print(
            "Successful: Functional dependencies provided.\n",
            style=successStyle
        )

        normalForm = inputparser.ReadNormalForm()
        console.print("Successful: Normal form provided.\n", style=successStyle)

        keys = inputparser.ReadKeys(relationInput.attributes)
        console.print("Successful: Keys provided.\n", style=successStyle)

        relationInput.keys = keys

        primaryKeyInput = inputparser.ReadPrimaryKey(relationInput)
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
    relationInput.SetPrimaryKey(primaryKeyInput)
    outputFileName = relationInput.name.lower() + ".sql"
    fullOutputFilePath = os.path.join(outputFilePath, outputFileName)

    print(f"Determining highest normal form of \"{relationInput.name}\"...")
    highestNormalForm = normalizer.DetermineHighestNormalForm(relationInput)
    console.print(
        f"The highest normal form of {relationInput.name} is {highestNormalForm}.",
        style=infoStyle
    )

    print(f"Normalizing relation \"{relationInput.name}\"...")

    normalizedRelations = normalizer.Normalize(relationInput, normalForm)
    querygenerator.GenerateQueryOutput(
        normalizedRelations,
        fullOutputFilePath
    )

    # try:
    #     normalizedRelations = normalizer.Normalize(relationInput, normalForm)
    #     querygenerator.GenerateQueryOutput(
    #         normalizedRelations,
    #         fullOutputFilePath
    #     )
    #    console.print(f"Finished normalization process.", style=successStyle)
    # except:
    #     console.print("There was an error normalizing the relation.", style=failureStyle)
    #     sys.exit()

if __name__ == "__main__":
    Main()
