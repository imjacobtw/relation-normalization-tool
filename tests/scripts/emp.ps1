$input = '..\relational-database-normalizer\tests\input\students.csv
Ename Pname Dname
exit
Ename Pname Dname
exit
Ename ->> Pname Dname
exit
4NF'

clear; $input | python .\src\main.py
