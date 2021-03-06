class StockDescription:
    def __init__(self, ticker, exchange):
        self.ticker = ticker
        self.exchange = exchange
        #TODO: Company name

    def __str__(self):
        return "Desc(Ticker={0}, Exchange={1})".format(self.ticker, self.exchange)

class StockCompanyProfile:
    def __init__(self, sector, industry, style):
        self.sector = sector
        self.industry = industry
        self.style = style #BUG HERE, if changed to Style - it fails

    def __str__(self):
        return "Profile(Sector={0}, Industry={1}, Style={2})".format(self.sector, self.industry, 'STYLE')

class StockData:
    def __init__(self, desc, profile):
        self.desc = desc
        self.profile = profile

    def __str__(self):
        return "Stock(Desc={0}, Profile={1})".format(self.desc, self.profile)