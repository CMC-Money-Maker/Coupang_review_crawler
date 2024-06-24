from pydantic import BaseModel


class Crawl_coupang_request(BaseModel):
    item_url: str
    page_count: int
