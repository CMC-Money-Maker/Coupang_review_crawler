import itertools

from src.application.coupang_review_crawler import Coupang_Crawler
from src.persistence.crawl_repository import Crawl_repository
from src.dto.crawl_coupang_request import Crawl_coupang_request

class Crawl_coupang_service:
    def __init__(self):
        self.coupang_cralwer = Coupang_Crawler()
        self.crawl_repository = Crawl_repository()
    def crawl_coupang(self, crawl_coupang_request: Crawl_coupang_request):
        crawl_data = self.coupang_cralwer.main(item_url=crawl_coupang_request.item_url, page_count=crawl_coupang_request.page_count)
        print("Crawl Finished, Now Writing to DB")
        db_dict = {
            "reviews": list(itertools.chain(*crawl_data))
        }
        self.crawl_repository.write_crawl_data(collection_name=crawl_coupang_request.item_url, data=db_dict)
