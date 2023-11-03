$input = '..\relation-normalizer\tests\input\students.csv
StudentID -> FirstName LastName
Course Professor -> Classroom
Course -> CourseStart CourseEnd
Professor -> ProfessorEmail
exit
BCNF
StudentID Course
exit
StudentID Course
..\relation-normalizer\tests\output'

clear; $input | python .\src\main.py