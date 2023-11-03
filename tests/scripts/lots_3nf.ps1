$input = '..\relation-normalizer\tests\input\lots_3nf.csv
PropertyID -> CountyName LotNumber Area Price TaxRate
CountyName LotNumber -> PropertyID Area Price TaxRate
CountyName -> TaxRate
Area -> Price
exit
3NF
PropertyID
CountyName LotNumber
exit
PropertyID
..\relation-normalizer\tests\output'

clear; $input | python .\src\main.py