import requests
import logging
import re
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urljoin


def scrape_page(url: str):
    logging.info(f'scraping {url}....')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error(f'get invalid status code {response.status_code} while scraping {url}')
    except requests.RequestException:
        logging.error(f'error occurred while scraping {url}', exc_info=True)


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info(f'get detail url {detail_url}')
        yield detail_url


def main():
    for page in range(1, TOTAL_PAGE+1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        logging.info(f'detail urls {list(detail_urls)}')


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
BASE_URL = 'https://static1.scrape.cuiqingcai.com'
TOTAL_PAGE = 10
if __name__ == '__main__':
    main()



