from get_detail_url import *


def scrap_detail(detail_url):
    return scrape_page(detail_url)


def parse_detail(html):
    doc = pq(html)
    cover = doc('.cover').attr('src')
    name = doc('.m-b-sm').text()
    categories = [item.text() for item in doc('.categories button span').items()]
    publish_at = doc('.info:contains(上映)').text()
    publish_at = re.search('(\d{4}-\d{2}-\d{2})', publish_at).group(1)\
        if re.search('(\d{4}-\d{2}-\d{2})', publish_at) else None
    drama = doc('.drama p').text()
    score = doc('.score').text()
    score = float(score) if score else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'publish_at': publish_at,
        'drama': drama,
        'score': score,
    }


def main():
    for page in range(1, TOTAL_PAGE+1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrap_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info(f'get detail info success {data}')


if __name__ == '__main__':
    main()

