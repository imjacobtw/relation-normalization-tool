from key import Key

import csv
import os


class Relation:
    def __init__(self):
        self.name = ""
        self.attributes = []
        self.keys = []
        self.primaryKey = None
        self.functionalDependencies = []

    def SetPrimaryKey(self, primaryKey):
        for key in self.keys:
            if primaryKey == key.attributes:
                key.isPrimary = True
                self.primaryKey = key

    def GetAttributesFromFile(filePath):
        with open(filePath) as file:
            csvReader = csv.reader(file)
            return next(csvReader)

    def GetNameFromFile(filePath):
        return os.path.splitext(os.path.basename(filePath))[0].upper()

    def __repr__(self):
        result = (
            f"Relation: {self.name}\n"
            f"Attributes: {self.attributes}\n"
            f"Functional Dependencies: {self.functionalDependencies}\n"
            f"Primary Key: {self.primaryKey}\n"
            f"Keys: {self.keys}\n"
        )

        return result
