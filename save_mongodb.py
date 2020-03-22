from get_detail_url import *
from get_detail_info import *


def save_data(data):
    global collection
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)  # 存在则更新，不存在则新建


def main():
    for page in range(1, TOTAL_PAGE+1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        for detail_url in detail_urls:
            detail_html = scrap_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info(f'get detail info success {data}')
            save_data(data)
            logging.info(f'data save successfully')


MONGODB_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGODB_DB_NAME = 'movies'
MONGODB_CONNECTION_NAME = 'movies'
client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
db = client[MONGODB_DB_NAME]
collection = db[MONGODB_CONNECTION_NAME]
if __name__ == '__main__':
    main()