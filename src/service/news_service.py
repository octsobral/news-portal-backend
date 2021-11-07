from src.database.repository.news_repository import NewsRepository
from src.schema.news import NewsInsert, NewsCustom
from datetime import datetime


class NewsService:
    def __init__(self):
        self.news_repository = NewsRepository()

    def create_news(self, news):
        self.news_repository.create_document(news)
        content = {'message': 'News saved successfully!'}
        return content

    def search_news(self, string):
        result = self.news_repository.find_contains(string)
        content = self._db_objects_to_schema(result)
        return content

    def get_all_news(self):
        result = self.news_repository.get_all()
        content = self._db_objects_to_schema(result)
        return content

    def get_news_by_id(self, document_id):
        match = {"id": document_id}
        content = self.news_repository.find(match)
        return content

    def edit_news(self, document_id, update):
        update = self._edited_handler(update)
        content = self.news_repository.update_document(document_id=document_id, update=update.dict(exclude_none=True))
        if content is None:
            content = {"message": "Could not update news. It may not exist."}
        else:
            content = {"message": "News updated"}
        return content

    def delete_news(self, document_id):
        content = self.news_repository.delete_document(document_id)
        if content is None:
            content = {"message": "Could not delete news. It may not exist."}
        else:
            content = {"message": "News deleted"}
        return content

    def _db_objects_to_schema(self, objects):
        content = []

        for document in objects:
            schema = NewsCustom(
                title=document.title,
                text=document.text,
                author=document.author,
                created=document.created,
                edited=document.edited,
                id=document.id
            )
            content.append(schema.dict())

        return content

    def _edited_handler(self, update):
        update_with_edited = NewsCustom()
        update_with_edited.title = update.title
        update_with_edited.text = update.text
        update_with_edited.author = update.author
        update_with_edited.edited = datetime.utcnow()
        return update_with_edited
