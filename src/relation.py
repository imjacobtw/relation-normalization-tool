import csv
import os

class Relation:
    @classmethod
    def __init__(self):
        self.name = ""
        self.attributes = []
        self.primaryKey = []
        self.functionalDependencies = []

    @staticmethod
    def GetAttributesFromFile(filePath):
        with open(filePath) as file:
            csvReader = csv.reader(file)
            return next(csvReader)
        
    @staticmethod
    def GetNameFromFile(filePath):
        return os.path.splitext(os.path.basename(filePath))[0].capitalize()
    
    @classmethod
    def __str__(self):
        resultString = f"Name: {self.name}\n"
        resultString += f"Attributes: {self.attributes}\n"
        resultString += f"Functional Dependencies: {self.functionalDependencies}\n"
        resultString += f"Primary Key: {self.primaryKey}"

        return resultString