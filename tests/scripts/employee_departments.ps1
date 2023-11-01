$input = 'C:\Users\ImJac\Code\Projects\relation-normalizer\tests\input\employee_departments.csv
Ssn -> Ename Bdate Address Dnumber
Dnumber -> Dname Dmgr_ssn
exit
3NF
Ssn
exit
Ssn
C:\Users\ImJac\Code\Projects\relation-normalizer\tests\output'

clear; $input | python .\src\main.py