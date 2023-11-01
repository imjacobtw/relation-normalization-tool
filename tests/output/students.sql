CREATE TABLE STUDENTS_1 (
	StudentID INT,
	Course VARCHAR(255),
	ProfessorEmail VARCHAR(255),
	PRIMARY KEY (StudentID, Course)
);

CREATE TABLE STUDENTS_2 (
	StudentID INT,
	FirstName VARCHAR(255),
	LastName VARCHAR(255),
	PRIMARY KEY (StudentID)
);

CREATE TABLE STUDENTS_3 (
	Course VARCHAR(255),
	CourseStart DATE,
	CourseEnd DATE,
	Professor VARCHAR(255),
	PRIMARY KEY (Course)
);

