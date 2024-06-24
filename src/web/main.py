import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from src.application.crawl_coupang_service import Crawl_coupang_service
from src.dto.crawl_coupang_request import Crawl_coupang_request

app = FastAPI()

@app.get("/", status_code=200)
def health_check():
    return "healthy"

@app.post("/crawl/coupang", status_code=200)
def crawl_coupang(crawl_coupang_request: Crawl_coupang_request):
    crawl_coupang_service = Crawl_coupang_service()
    crawl_coupang_service.crawl_coupang(crawl_coupang_request)
    return "crawled success"

handler = Mangum(app)
