import requests

from bs4 import BeautifulSoup


URL = 'https://hh.ru/search/vacancy?text=python&'

HEADERS = {
        'Host': 'hh.ru',
        'User-Agent': 'Safari',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }


def max_page():
    search_requests = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(search_requests.text, 'html.parser')
    paginator = soup.find_all('span', {'class': "pager-item-not-in-short-range"})
    pages = []

    for page in paginator:
        pages.append(int(page.find('a').text))

    return pages[-1]


def vacancy(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f'{URL}&page={page}', headers=HEADERS)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': "serp-item"})
        for result in results:
            title = result.find('a').text
            company =result.find('div', {'class': "vacancy-serp-item__meta-info-company"}).find('a').text
            price = result.find('span', {'class': 'bloko-header-section-3'})
            jobs.append([title, company, price])
    print(jobs)

