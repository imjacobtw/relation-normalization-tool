$input = '..\relation-normalizer\tests\input\employee_departments.csv
Ssn -> Ename Bdate Address Dnumber
Dnumber -> Dname Dmgr_ssn
exit
3NF
Ssn
exit
Ssn
..\relation-normalizer\tests\output'

clear; $input | python .\src\main.py