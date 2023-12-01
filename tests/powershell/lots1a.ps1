$input = '..\relational-database-normalizer\tests\input\lots1a.csv
PropertyID
CountyName LotNumber
exit
PropertyID
PropertyID -> CountyName LotNumber Area
CountyName LotNumber -> PropertyID Area
Area -> CountyName
exit
exit
BCNF'

clear; $input | python .\src\main.py
