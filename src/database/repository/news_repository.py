import mongoengine as mongo
from mongoengine.queryset.visitor import Q

from src.database.model.news import News
from src.database.repository.repository import Repository


class NewsRepository(Repository):
    def __init__(self):
        super().__init__(model=News)

    def find_contains(self, string: str):
        try:
            return list(
                self.model.objects(Q(title__contains=string) | Q(text__contains=string) | Q(author__contains=string))
            )
        except mongo.DoesNotExist:
            return None

    def create_document(self, schema: News):
        new_document = self.model()
        new_document.title = schema.title
        new_document.text = schema.text
        new_document.author = schema.author
        new_document.save()

