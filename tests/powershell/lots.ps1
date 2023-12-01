$input = '..\relational-database-normalizer\tests\input\lots.csv
PropertyID
CountyName LotNumber
exit
PropertyID
PropertyID -> CountyName LotNumber Area Price TaxRate
CountyName LotNumber -> PropertyID Area Price TaxRate
CountyName -> TaxRate
Area -> Price
exit
exit
3NF'

clear; $input | python .\src\main.py
