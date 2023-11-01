$input = 'C:\Users\ImJac\Code\Projects\relation-normalizer\tests\input\employee_projects.csv
Ssn Pnumber -> Hours
Ssn -> Ename
Pnumber -> Pname Plocation
exit
3NF
Ssn Pnumber
exit
Ssn Pnumber
C:\Users\ImJac\Code\Projects\relation-normalizer\tests\output'

clear; $input | python .\src\main.py