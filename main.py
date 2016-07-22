from stock import StockDescription, StockData
from data_service import *
from portfolio_creator import *
from csv_generator import *


if __name__ == '__main__':

    #step 1. define portfolio
    #portfolio = [
    #    StockDescription('AAPL', 'XNAS'),
    #    StockDescription('FB', 'XNAS'),
    #    StockDescription('ATVI','XNAS')
    #]

    portfolio = create_portfolio(True)

    # step2. load data
    for s in portfolio:
        profile = company_profile(s)
        print(str(StockData(s, profile)))

    # step3. calculate
    #nothing to calculate

    #step4. ???? create one object from different outputs??

    #step5. generate output

    generate_csv(portfolio)

