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
- Fourth and fifth normal form conversion has not been implemented.
- PEP 8 guidelines were not completely followed. I do not expect this project to become a prominent library that other developers maintain.

Features to add/modify:
- Fourth and fifth normal form conversion options.
- Code restructure to improve readability and modularlity.

## Demo
Given the file [tests/input/lots_3nf.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/lots_3nf.csv), here is a demo of the program.

The relation given as input:
##### LOTS_3NF
| *PropertyID* | CountyName | LotNumber | Area | Price | TaxRate |
|--------------|------------|-----------|------|-------|---------|

```
Please provide the absolute path to the CSV file with the relation you want to normalize:
..\relation-normalizer\tests\input\lots_3nf.csv
Successful: CSV file provided.

Please provide the functional dependencies of the relation (type "exit" when finished):
Format: attribute1 -> attribute2 ... attributeN
PropertyID -> CountyName LotNumber Area Price TaxRate
CountyName LotNumber -> PropertyID Area Price TaxRate
CountyName -> TaxRate
Area -> Price
exit
Successful: Functional dependencies provided.

Please provide the normal form you want to the relation to be in (1NF, 2NF, 3NF, BCNF, 4NF, 5NF):
3NF
Successful: Normal form provided.

Please provide all of the candidate keys (type "exit" when finished):
Format: attribute1 ... attributeN
PropertyID
CountyName LotNumber
Successful: Keys provided.

Please provide the primary key of the relation:
Format: attribute1 ... attributeN
PropertyID
Successful: Primary key provided.

Please provide the absolute path to the directory for the output:
Successful: Output file path provided.

Determining highest normal form of "LOTS_3NF"...
The highest normal form of LOTS_3NF is 1NF.
Normalizing relation "LOTS_3NF"...
Finished normalization process.
```

The tables given after a third normal form conversion:
##### LOTS_3NF_3
| *PropertyID* | CountyName | LotNumber | Area |
|------------|------------|-----------|--------|

##### LOTS_3NF_2
| *CountyName* | TaxRate |
|--------------|---------|

##### LOTS_3NF_4
| *Area* | Price |
|--------|-------|

The SQL statements to create the tables:
```
CREATE TABLE LOTS_3NF_3 (
	PropertyID INT,
	CountyName VARCHAR(255),
	LotNumber INT,
	Area VARCHAR(255),
	PRIMARY KEY (PropertyID)
);

CREATE TABLE LOTS_3NF_2 (
	CountyName VARCHAR(255),
	TaxRate REAL,
	PRIMARY KEY (CountyName)
);

CREATE TABLE LOTS_3NF_4 (
	Area VARCHAR(255),
	Price REAL,
	PRIMARY KEY (Area)
);
```

## Tests
I have provided many PowerShell scripts for testing first, second, third, and Boyce-Codd normal forms in [tests/scripts](https://github.com/imjacobtw/relation-normalizer/tree/main/tests/scripts). You will have to adjust the scripts to use the absolute file paths to the input on your machine if you intend to run the automated tests yourself. The input relations can be found in [tests/input](https://github.com/imjacobtw/relation-normalizer/tree/main/tests/input). These are the normal forms each relation tests for:
- [employee_departments.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/employee_departments.csv) (Third Normal Form)
- [employee_projects.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/employee_projects.csv) (Second Normal Form)
- [lots_3nf.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/lots_3nf.csv) (Third Normal Form)
- [lots_bcnf.csv](https://github.com/imjacobtw/relation-normalizer/blob/main/tests/input/lots_bcnf.csv) (Boyce-Codd Normal Form)

The images in [docs](https://github.com/imjacobtw/relation-normalizer/tree/main/docs) give a visual representation for all of these tests. All of these examples are provided by *Fundamentals of Database Systems 7th Edition by Elmasri and Navathe.*