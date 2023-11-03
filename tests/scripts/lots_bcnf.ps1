$input = '..\relation-normalizer\tests\input\lots_bcnf.csv
PropertyID -> CountyName LotNumber Area
CountyName LotNumber -> PropertyID Area
Area -> CountyName
exit
BCNF
PropertyID
CountyName LotNumber
exit
PropertyID
..\relation-normalizer\tests\output'

clear; $input | python .\src\main.py