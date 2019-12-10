import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user - agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

base_url = 'https://hh.ru/search/vacancy?area=1&search_period=3&text=python&page=0'

def hh_parse(base_url, headers):
    session = requests.Session()
    requests = session.get(base_url, headers=headers)
    if requests.status_code == 200:
        print('OK')
    else:
        print('ERROR)

print(requests.status_code)
hh_parse(base_url, headers)

