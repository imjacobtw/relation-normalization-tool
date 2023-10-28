# Relation Normalizer
A Python script that takes a relation and functional dependencies as input, normalizes the relation based on the provided functional dependencies, and produces SQL queries to generate the normalized database tables. This is an assignment for COMP SCI 5300 at Missouri S&amp;T.

## Project Outline
Information regarding the assignment details can be found in [docs/project.pdf](https://github.com/imjacobtw/relation-normalizer/blob/main/docs/project.pdf).

## Usage
Install the dependencies:
```
pip install -r requirements.txt
```

Run the script:
```
python src/main.py
```

## Demo
Given the file [tests/input/students.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/students.csv), a demo of the script may look like this:
```
Please provide the absolute path to the CSV file with the relation you want to normalize:
..\relation-normalizer\tests\input\students.csv
Successful: CSV file provided.

Please provide the functional dependencies of the relation (type "exit" when finished):
Format: attribute1 -> attribute2 ... attributeN
StudentID -> FirstName                                                    
exit
Successful: Functional dependencies provided.

Please provide the normal form you want to the relation to be in (1NF, 2NF, 3NF, BCNF, 4NF, 5NF):
1NF                                                                       
Successful: Normal form provided.

Please provide the primary/composite key of the relation:
Format: attribute1 ... attributeN
StudentID
Successful: Primary key provided.
```