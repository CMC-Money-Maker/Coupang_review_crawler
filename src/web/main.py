import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from src.application.crawl_coupang_service import Crawl_coupang_service
from src.dto.crawl_coupang_request import Crawl_coupang_request

app = FastAPI()

@app.post("/crawl/coupang", status_code=200)
def crawl_coupang(crawl_coupang_request: Crawl_coupang_request):
    crawl_coupang_service = Crawl_coupang_service()
    crawl_coupang_service.crawl_coupang(crawl_coupang_request)
    return "crawled success"

@app.on_event("startup")
def startup_event():
    import os
    app.state.KAKAO_API_KEY = os.getenv("MONGODB_PW")

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
