from stock import *


def create_portfolio(fake_portfolio):
    stocks = []
    if fake_portfolio:
        nasdaq_tickers_file = open('test_tickers.txt', 'r')
    else:
        nasdaq_tickers_file = open('nasdaq_tickers.txt', 'r')
    for line in nasdaq_tickers_file:
        data = line.split()
        stocks.append(StockDescription(data[0], data[1]))
    return stocks
