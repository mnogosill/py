import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

base_url = 'https://hh.ru/search/vacancy?area=&search_period=30&text=python&page=0'

def hh_parse(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_premium'})
        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            location = div.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text
            respons = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            requir =  div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            content = respons + ' ' + requir
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'location': location,
                'content': content
            })
        print(jobs)
    else:
        print('ERROR')

hh_parse(base_url, headers)

