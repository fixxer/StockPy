import csv
from stock import *

def generate_csv(portfolio):
    with open('Stocks.csv', 'wb') as csvfile:
        datawriter = csv.writer(csvfile)
        for s in portfolio:
            datawriter.writerow([s.ticker] + [s.exchange])