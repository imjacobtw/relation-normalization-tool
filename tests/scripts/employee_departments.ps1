$input = '..\relational-database-normalizer\tests\input\employee_departments.csv
Ssn
exit
Ssn
Ssn -> Ename Bdate Address Dnumber
Dnumber -> Dname Dmgr_ssn
exit
exit
3NF'

clear; $input | python .\src\main.py
