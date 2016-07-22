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
    stockPBs = soup.div.table.tbody.find_all('tr')[4].find_all('td')
    pb_values = [v.text for v in stockPBs]
    return pe_values, pb_values

def get_current_valuation(stock_desc):
    soup = get_soup('http://financials.morningstar.com/valuate/current-valuation-list.action?&t={0}:{1}', stock_desc.exchange, stock_desc.ticker)
    #current PE
    #current PB
    #Divident Yield
    #industry average PE
    #industry average PB

    #var tr = from el in root.Element("tbody").Elements("tr") where (string)el.Element("th") == @"Price/Earnings" select el;
    #var tds = tr.Elements("td");
    #var stockPE = tds.ElementAt(0).Value;
    #var industryPE = tds.ElementAt(1).Value;

    #var tr = from el in root.Element("tbody").Elements("tr") where (string)el.Element("th") == @"Price/Book" select el;
    #var tds = tr.Elements("td");
    #var stockPB = tds.ElementAt(0).Value;
    #var industryPB = tds.ElementAt(1).Value;

    #var tr = from el in root.Element("tbody").Elements("tr") where (string)el.Element("th") == @"Dividend Yield %" select el;
    #var tds = tr.Elements("td");
    #var dividents = tds.ElementAt(0).Value;

def download_yahoo_prices(s, startYear, endYear):
    path = 'http://real-chart.finance.yahoo.com/table.csv'
    param = '?s=' + s.ticker + '&a=00&b=1&c=' + startYear + '&d=11&e=31&f=' + endYear + '&g=d&ignore=.csv'
    path += param
    #return CSV file

if __name__ == '__main__':
    #print company_profile('XNAS', 'FB')
    print(GetHistoricalMorningstarData(StockDescription('FB', 'XNAS')))