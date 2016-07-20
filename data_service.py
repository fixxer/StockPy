from bs4 import BeautifulSoup
import requests
from Stock import StockDescription


def get_soup(base_url, *args):
    url = base_url.format(*args)
    html = requests.get(url).text
    return BeautifulSoup(html, 'html5lib')


def company_profile(exchange, ticker):
    soup = get_soup(
        'http://financials.morningstar.com/cmpind/company-profile/component.action?component=BasicData&t={0}:{1}',
        exchange, ticker)
    rows = soup.tbody.find_all('tr')
    sector_and_industry = rows[5].find_all('td')
    return {
        'Sector': sector_and_industry[2].text,
        'Industry': sector_and_industry[4].text,
        'Style': rows[8].find_all('td')[0].text
    }


def company_profile_stock(s):
    soup = get_soup('http://financials.morningstar.com/cmpind/company-profile/component.action?component=BasicData&t={0}:{1}', s.exchange, s.ticker)
    rows = soup.tbody.find_all('tr')
    sector_and_industry = rows[5].find_all('td')
    return {
    'Sector': sector_and_industry[2].text,
    'Industry': sector_and_industry[4].text,
    'Style': rows[8].find_all('td')[0].text
    }

if __name__ == '__main__':
    print company_profile('XNAS', 'FB')
