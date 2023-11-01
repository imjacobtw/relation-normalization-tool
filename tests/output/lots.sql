CREATE TABLE LOTS_1 (
	PropertyID INT,
	CountyName VARCHAR(255),
	LotNumber INT,
	Area VARCHAR(255),
	Price VARCHAR(255),
	PRIMARY KEY (PropertyID)
);

CREATE TABLE LOTS_2 (
	CountyName VARCHAR(255),
	TaxRate VARCHAR(255),
	PRIMARY KEY (CountyName)
);

