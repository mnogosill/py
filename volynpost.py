import requests
import csv
from bs4 import BeautifulSoup as bs

# ------------------подключеные модули

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

base_url = 'http://www.volynpost.com/search/%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82+%D1%83+%D0%9B%D1%83%D1%86%D1%8C%D0%BA%D1%83+%D0%BD%D0%B0+/1'


def vp_parse(base_url, headers):
    kurses = []  # чистый список работ
    #urls = []  # чистый список страниц
    #urls.append(base_url)  # добавляем первую страницу
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:  # проверка жива ли страница
        soup = bs(request.content, 'lxml')  # парсер
        divs = soup.find_all('div', attrs=('content'))
        for div in divs:
            divs_cont = div.find('div')

    print(divs_cont)


vp_parse(base_url, headers)