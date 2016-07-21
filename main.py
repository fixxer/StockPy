import csv
from stock import StockDescription, StockData
from data_service import *

if __name__ == '__main__':

    #step 1. define portfolio
    portfolio = [
        StockDescription('AAPL', 'XNAS'), 
        StockDescription('FB', 'XNAS'), 
        StockDescription('ATVI','XNAS')
    ]

    # step2. load data
    for s in portfolio:
        profile = company_profile(s)
        print(str(StockData(s, profile)))

    # step3. calculate
    #nothing to calculate

    #step4. ???? create one object from different outputs??

    #step5. generate output

    with open('Stocks.csv', 'wb') as csvfile:
        datawriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for s in portfolio:
            outputString = s.ticker + ';'
            datawriter.writerow([s.ticker])

