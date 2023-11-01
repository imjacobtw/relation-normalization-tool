CREATE TABLE EMPLOYEE_PROJECTS_1 (
	Ssn VARCHAR(255),
	Pnumber INT,
	Hours INT,
	PRIMARY KEY (Ssn, Pnumber)
);

CREATE TABLE EMPLOYEE_PROJECTS_2 (
	Ssn VARCHAR(255),
	Ename VARCHAR(255),
	PRIMARY KEY (Ssn)
);

CREATE TABLE EMPLOYEE_PROJECTS_3 (
	Pnumber INT,
	Pname VARCHAR(255),
	Plocation VARCHAR(255),
	PRIMARY KEY (Pnumber)
);

