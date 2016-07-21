from stock import *


def create_portfolio(fake_portfolio):
    stocks = []
    if fake_portfolio == 1:
        nasdaq_tickers_file = open('test_tickers.txt', 'r')
    else:
        nasdaq_tickers_file = open('nasdaq_tickers.txt', 'r')
    for line in nasdaq_tickers_file:
        stocks.append(StockDescription(line, 'XNAS'))
    return stocks
