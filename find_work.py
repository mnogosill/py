import requests
import csv
from bs4 import BeautifulSoup as bs

# ------------------подключеные модули

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

base_url = 'https://hh.ru/search/vacancy?area=&search_period=7&text=python&page=0'


# -------------вводные данные {'браузер', 'сайт'}

def hh_parse(base_url, headers):
    jobs = []  # чистый список работ
    urls = []  # чистый список страниц
    urls.append(base_url)  # добавляем первую страницу
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:  # проверка жива ли страница
        soup = bs(request.content, 'lxml')  # парсер
        try:  # -----------------проверка на количество страниц
            pagination = soup.find_all('a', attrs={'data-qa': 'pager-page'})
            count = int(pagination[-1].text)
            for i in range(count):
                url = f'https://hh.ru/search/vacancy?area=&search_period=7&text=python&page={i}'
                if url not in urls:  # проверка на ссылку в списке
                    urls.append(url)  # добавить есои нету
        except:
            pass  # если есть то дальше
    for url in urls:  # для каждой ссылки в списке
        request = session.get(url, headers=headers)  # ответ сервера
        soup = bs(request.content, 'lxml')  # парсер
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_premium'})
        for div in divs:  # для каждого дива
            try:        #проверить на наличие данных
                title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
                #href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
                #company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
                #location = div.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text
                #respons = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
                #requir = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
                #content = respons + ' ' + requir
                # try:
                jobs.append({  # добавить в список jobs работы по типажу ниже
                    'title': title,
                    #'href': href,
                    #'company': company,
                    #'location': location,
                    #'content': content
                })
            except:
                pass
        #print(jobs)
        #print(len(jobs))
           # print(len(jobs))
            #print(jobs)
        print(len(jobs))
    else:
        print(request.status_code)
hh_parse(base_url, headers)
'''return jobs

def file_writer(jobs):
    with open('parsed-jobs2.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('Title', 'Link', 'Company', 'Location', 'Respons&Requists'))
        for job in jobs:
            writer.writerow((job['title'], job['href'], job['company'], job['location'], job['content']))



jobs = hh_parse(base_url, headers)
file_writer(jobs)'''