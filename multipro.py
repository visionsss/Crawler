import multiprocessing
from save_mongodb import *


def main(page):
    """爬取每页的操作"""
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrap_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info(f'get detail info success {data}')
        save_data(data)
        logging.info(f'data save successfully')


if __name__ == '__main__':
    pool = multiprocessing.Pool()  # 创建进程池
    pages = range(1, TOTAL_PAGE + 1)    # main的参数
    pool.map(main, pages)   # 映射，如(main(pages[0], main(pages[1], ....))
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
