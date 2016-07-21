import csv
from stock import *

def generate_csv(portfolio):
    with open('Stocks.csv', 'wb') as csvfile:
        datawriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for s in portfolio:
            #outputString = s.desc.ticker + ';'
            datawriter.writerow([s.ticker])