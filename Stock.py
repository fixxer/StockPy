class StockDescription:
    def __init__(self, ticker, exchange):
        self.ticker = ticker  # instance variable unique to each instance
        self.exchange = exchange

    def __str__(self):
        return "Ticker: {0}, Exchange: {1}".format(self.ticker, self.exchange)

class StockData:
    def __init__(self, desc, sector, industry, style):
        self.desc = desc
        self.sector = sector
        self.industry = industry
        self.style = sector

    def __str__(self):
        return "Desc: {0}; Sector: {1}, Industry: {2}, Style: {3}".format(self.desc, self.sector, self.industry, self.style)