import csv
from Stock import *
from data_service import *

if __name__ == '__main__':

    #step 1. define portfolio
    stock1 = StockDescription('AAPL', 'XNAS')
    stock2 = StockDescription('FB', 'XNAS')

    stocks = [stock1, stock2, StockDescription('ATVI','XNAS')]

    # step2. load data
    #for s in stocks:
    #    print(s.ticker+': -> '+str(company_profile_stock(s)))

    for s in stocks:
        profile = company_profile_stock(s)
        print(str(StockData(s, profile['Industry'], profile['Sector'], profile['Style'])))

    # step3. calculate
    #nothing to calculate

    #step4. ???? create one object from different outputs??

    #step5. generate output

    with open('Stocks.csv', 'wb') as csvfile:
        datawriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for s in stocks:
            outputString = s.ticker + ';'
            datawriter.writerow([s.ticker])

