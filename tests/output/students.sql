CREATE TABLE Students (
	StudentID INT,
	FirstName VARCHAR(255),
	LastName VARCHAR(255),
	Course VARCHAR(255),
	Professor VARCHAR(255),
	ProfessorEmail VARCHAR(255),
	CourseStart DATE,
	CourseEnd DATE,
	PRIMARY KEY (StudentID, Course)
);

