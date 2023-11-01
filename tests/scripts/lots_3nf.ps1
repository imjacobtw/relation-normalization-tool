$input = 'C:\Users\ImJac\Code\Projects\relation-normalizer\tests\input\lots_3nf.csv
PropertyID -> CountyName LotNumber Area
CountyName LotNumber -> PropertyID Area
Area -> CountyName
exit
3NF
PropertyID
CountyName LotNumber
exit
PropertyID
C:\Users\ImJac\Code\Projects\relation-normalizer\tests\output'

clear; $input | python .\src\main.py