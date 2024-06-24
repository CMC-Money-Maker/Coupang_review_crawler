import uvicorn
from fastapi import FastAPI

from src.coupang_review_crawler import Coupang
from src.dto.crawl_coupang_request import Crawl_coupang_request

app = FastAPI()

@app.post("/crawl/coupang", status_code=200)
async def crawl_coupang(crawl_coupang_request: Crawl_coupang_request):
    coupang = Coupang()
    response = Coupang.main(coupang, item_url=crawl_coupang_request.item_url, page_count=crawl_coupang_request.page_count)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
