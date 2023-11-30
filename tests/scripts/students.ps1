$input = '..\relational-database-normalizer\tests\input\students.csv
StudentID Course
exit
StudentID Course
StudentID -> FirstName LastName
Course Professor -> ClassRoom
Course -> CourseStart CourseEnd
Professor -> ProfessorEmail
exit
Course ->> Professor ClassRoom
StudentID ->> Course Professor
exit
BCNF'

clear; $input | python .\src\main.py
