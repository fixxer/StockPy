import csv

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker  # instance variable unique to each instance

#ah so

if __name__ == '__main__':

    stock1 = Stock('AAPL')
    stock2 = Stock('FB')

    stocks = [stock1, stock2]

    with open('test.csv', 'wb') as csvfile:
        datawriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for s in stocks:
            datawriter.writerow([s.ticker])

