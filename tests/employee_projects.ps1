$input = '..\relational-database-normalizer\tests\input\employee_projects.csv
Ssn Pnumber
exit
Ssn Pnumber
Ssn Pnumber -> Hours
Ssn -> Ename
Pnumber -> Pname Plocation
exit
exit
2NF'

clear; $input | python .\src\main.py
