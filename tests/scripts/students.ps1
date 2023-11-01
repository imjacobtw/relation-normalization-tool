$input = 'C:\Users\ImJac\Code\Projects\relation-normalizer\tests\input\students.csv
StudentID -> FirstName LastName
Course -> CourseStart CourseEnd Professor
Professor -> ProfessorEmail
exit
2NF
StudentID Course
exit
StudentID Course
C:\Users\ImJac\Code\Projects\relation-normalizer\tests\output'

clear; $input | python .\src\main.py