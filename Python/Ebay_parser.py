import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://www.ebay.com'
URL = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=valve+train+chain&_sacat=0' # сюда прописать ссылку из поиска Ebay
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}       # актуальные можно взять с хедеров Ebay


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='s-item__info clearfix')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('a', class_='s-item__link').find('h3',
                                                                    class_='s-item__title').get_text(),
                'price': item.find('div', class_='s-item__details clearfix').find('div',
                                                                                  class_='s-item__detail '
                                                                                         's-item__detail--primary').find(
                    'span', class_='s-item__price').get_text().replace('$', '').replace(' руб.', ''),
                'link_prod': item.find('a', class_='s-item__link').get('href')
            }
        )
    return cards


def save_doc(items, path):
    with open(path, 'w', newline='') as file:  # может запросить кодировку , encoding='utf8'
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Title', 'Price', 'Link'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['link_prod']])


def parser():
    PAGENATION = input('Specify the number of pages to parse: ')
    PAGENATION = int(PAGENATION.strip())
    # PAGENATION = xx # - можно тут количество страниц для парсинга прописать, если не прокатывают строки выше
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION + 1):
            print(f'Parsing the page: {page}')
            html = get_html(URL, params={'_pgn': page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
    else:
        print('Error')


parser()
