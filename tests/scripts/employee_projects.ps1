$input = '..\relation-normalizer\tests\input\employee_projects.csv
Ssn Pnumber -> Hours
Ssn -> Ename
Pnumber -> Pname Plocation
exit
2NF
Ssn Pnumber
exit
Ssn Pnumber
..\relation-normalizer\tests\output'

clear; $input | python .\src\main.py