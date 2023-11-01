# Relation Normalizer
A Python script that takes a relation and functional dependencies as input, normalizes the relation based on the provided functional dependencies, and produces SQL queries to generate the normalized database tables. This is an assignment for COMP SCI 5300 at Missouri S&amp;T.

## Usage
Install the dependencies:
```
pip install -r requirements.txt
```

Run the script:
```
python src/main.py
```

## Description
Information regarding the assignment details can be found in [docs/project.pdf](https://github.com/imjacobtw/relation-normalizer/blob/main/docs/project.pdf).

Details to note:
- Given CSV relation must already be in first normal form due to the standard of comma-separated value files.
- Attribute types are inferred from the given names of the attributes.
- PEP 8 guidelines were not completely followed. I do not expect this project to become a prominent library that other developers maintain.

Features to add:
- Fourth and fifth normal form conversion options.

## Demo
Given the file [tests/input/employee_projects.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/employee_projects.csv), a demo of the script may look like this:
```
Please provide the absolute path to the CSV file with the relation you want to normalize:
..\relation-normalizer\tests\input\employee_projects.csv
Successful: CSV file provided.

Please provide the functional dependencies of the relation (type "exit" when finished):
Format: attribute1 -> attribute2 ... attributeN
Ssn Pnumber -> Hours
Ssn -> Ename
Pnumber -> Pname Plocation                                                  
exit
Successful: Functional dependencies provided.

Please provide the normal form you want to the relation to be in (1NF, 2NF, 3NF, BCNF, 4NF, 5NF):
2NF                                                                       
Successful: Normal form provided.

Please provide all of the candidate keys (type "exit" when finished):    
Format: attribute1 ... attributeN
Ssn Pnumber
Successful: Keys provided.

Please provide the primary/composite key of the relation:
Format: attribute1 ... attributeN
Ssn Pnumber
Successful: Primary key provided.

Please provide the absolute path to the directory for the output:
..\relation-normalizer\tests\output
Successful: Output file path provided.

Normalizing relation "EMPLOYEE_PROJECTS"...
Finished normalization process.
```

## Tests
..