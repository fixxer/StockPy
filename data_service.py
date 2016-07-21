from bs4 import BeautifulSoup
import requests
from stock import StockDescription, StockCompanyProfile

def get_soup(base_url, *args):
    url = base_url.format(*args)
    html = requests.get(url).text
    return BeautifulSoup(html, 'html5lib')

def company_profile(stock_desc):
    soup = get_soup(
        'http://financials.morningstar.com/cmpind/company-profile/component.action?component=BasicData&t={0}:{1}',
        stock_desc.exchange, stock_desc.ticker)
    rows = soup.tbody.find_all('tr')
    sector_and_industry = rows[5].find_all('td')
    sector = sector_and_industry[2].text
    industry = sector_and_industry[4].text
    style = rows[8].find_all('td')[0].text
    return StockCompanyProfile(sector, industry, style)

def GetHistoricalMorningstarData(stockDesc):
    path = 'http://financials.morningstar.com/valuate/valuation-history.action?&t={0}:{1}&type=price-earnings'
    soup = get_soup(path, stockDesc.exchange, stockDesc.ticker)
    stockPEs = soup.div.table.tbody.find_all('tr')[1].find_all('td')
    pe_values = [v.text for v in stockPEs]
    return pe_values

if __name__ == '__main__':
    #print company_profile('XNAS', 'FB')
    print(GetHistoricalMorningstarData(StockDescription('FB', 'XNAS')))