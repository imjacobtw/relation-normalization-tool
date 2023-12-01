# Relational Database Normalizer
A Python script that takes a relation schema and its constraints as input, normalizes the schema to a desired normal form, and outputs the necessary SQL statements to generate the normalized relation schemas.

## Usage
### Install the Dependencies
Using `pip` directly:
```
pip install -r requirements.txt
```

Using `make` targets:
```
make init
```


### Run the Script
Using `python` directly:
```
python src/main.py
```

Using `make` targets:
```
make run
```

### Run the Tests
Using `pytest` directly:
```
pytest
```

Using `make` targets:
```
make test
```

## Description
This was an assignment for COMP SCI 5300 at Missouri S&T. Due to time contraints, I did not have time to implement all the necessary normal form conversions. Since normal forms higher than BCNF are often not practically used, I decided to implement up to BCNF. I plan to come back to this project and implement 4NF, 5NF, and 6NF at a minimum.

Details to note:
- Given CSV relation must already be in first normal form due to the standard of comma-separated value files.
- Attribute types are heuristically generated from the given names of the attributes.
- Supports up to 1NF, 2NF, 3NF, and BCNF conversion.
- Utilizes PyTest for unit testing and Rich for displaying colored formatting in the terminal.

Features to add/modify:
- Higher normal form conversion options.
- Code restructure to improve readability and modularlity.

## Demo
Given the file [tests/input/lots.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/lots.csv), here is a demo of the program.

The relation given as input:
##### LOTS
| *PropertyID* | CountyName | LotNumber | Area | Price | TaxRate |
|--------------|------------|-----------|------|-------|---------|

```
Provide the path to the file with the relation(s) you want to normalize:
[success] CSV file provided.
[success] Relation name parsed.
[success] Attributes parsed.

Provide all of the candidate keys (type "exit" when finished):  
Format: attribute1 ... attributeN
[success] Candidate keys provided.

Provide the primary key (type "exit" when finished):
Format: attribute1 ... attributeN
[success] Primary key provided.

Provide the functional dependencies (type "exit" when finished):
Format: LAttribute1 ... LAttributeN -> RAttribute1 ... RAttributeN
[success] Functional dependencies provided.

Provide the multivalued dependencies (type "exit" when finished):
Format: LAttribute1 ... LAttributeN ->> RAttribute1 ... RAttributeN
[success] Multivalued dependencies provided.

The normal form to convert the relation into:
The available normal forms: (UNF, 1NF, 2NF, 3NF, BCNF, 4NF)
[success] Normal form provided.

[notice] CSV files will have heuristically generated SQL data types. It is recommended to review the data types for the attributes after the normalization process.
[notice] CSV relation schemas are automatically in 1NF due to the standard of CSV files.

Beginning normalization process...

Converting LOTS to 2NF...
  Dependency that violates 2NF: (CountyName -> TaxRate)
        Creating relation LOTS_1...
[success] 2NF conversion completed.

Converting LOTS to 3NF...
  Dependency that violates 3NF: (Area -> Price)
        Creating relation LOTS_2...
Converting LOTS_1 to 3NF...
  LOTS_1 is already in 3NF.
[success] 3NF conversion completed.

[success] Normalization process complete.

CREATE TABLE LOTS (
        PropertyID INT,
        CountyName VARCHAR(255),
        LotNumber INT,
        Area VARCHAR(255),
        PRIMARY KEY (PropertyID)
);

CREATE TABLE LOTS_1 (
        CountyName VARCHAR(255),
        TaxRate REAL,
        PRIMARY KEY (CountyName)
);

CREATE TABLE LOTS_2 (
        Area VARCHAR(255),
        Price REAL,
        PRIMARY KEY (Area)
);
```

The tables given after a third normal form conversion:
##### LOTS
| *PropertyID* | CountyName | LotNumber | Area |
|------------|------------|-----------|--------|

##### LOTS_1
| *CountyName* | TaxRate |
|--------------|---------|

##### LOTS_2
| *Area* | Price |
|--------|-------|

## Tests
I have provided many Pytest and PowerShell scripts for testing first, second, third, and Boyce-Codd normal forms in [tests](https://github.com/imjacobtw/relation-normalizer/tree/main/tests/). The input relations can be found in [tests/input](https://github.com/imjacobtw/relation-normalizer/tree/main/tests/input). These are the normal forms each relation tests for:
- [employee_departments.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/employee_departments.csv) (Third Normal Form)
- [employee_projects.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/employee_projects.csv) (Second Normal Form)
- [lots.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/lots.csv) (Third Normal Form)
- [lots1a.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/lots1a.csv) (Boyce-Codd Normal Form)

All of these examples are from Chapter 14 of *Fundamentals of Database Systems 7th Edition by Elmasri and Navathe.*