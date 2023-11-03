CREATE TABLE STUDENTS_4 (
	StudentID INT,
	Course VARCHAR(255),
	Professor VARCHAR(255),
	Classroom VARCHAR(255),
	PRIMARY KEY (StudentID, Course)
);

CREATE TABLE STUDENTS_5 (
	Professor VARCHAR(255),
	ProfessorEmail VARCHAR(255),
	PRIMARY KEY (Professor)
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
	PRIMARY KEY (Course)
);