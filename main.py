import uvicorn
from fastapi import FastAPI

from src.config.config import Config
from src.database.database import Database
from src.service.news_service import NewsService
from src.schema.news import NewsInsert, NewsUpdate

app = FastAPI()
config = Config()
database = Database(config=config)
news_service = NewsService()


@app.get('/news', tags=['news'])
def list_news():
    content = news_service.get_all_news()
    return content


@app.post('/news', tags=['news'])
def create_news(news: NewsInsert):
    content = news_service.create_news(news)
    return content


@app.get('/news/{search}', tags=['news'])
def search_news(search: str):
    content = news_service.search_news(search)
    return content


@app.put('/news/{document_id}', tags=['news'])
def edit_news(document_id, update: NewsUpdate):
    content = news_service.edit_news(document_id, update)
    return content


@app.delete('/news/{document_id}', tags=['news'])
def delete_news(document_id):
    content = news_service.delete_news(document_id)
    return content


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

