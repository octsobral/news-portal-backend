from abc import ABC, abstractmethod
import mongoengine as mongo


class Repository(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def create_document(self, schema):
        return NotImplementedError

    @abstractmethod
    def find_contains(self, search):
        return NotImplementedError

    def get_all(self):
        try:
            return list(self.model.objects())
        except mongo.DoesNotExist:
            return None

    def find(self, kwargs):
        try:
            return self.model.objects.get(**kwargs)
        except mongo.DoesNotExist:
            return None

    def update_document(self, document_id, update):
        try:
            return self.model.objects(id=document_id).update_one(**update)
        except mongo.DoesNotExist:
            return None

    def delete_document(self, document_id):
        try:
            document = self.model.objects(id=document_id)
            document.delete()
            return True
        except mongo.DoesNotExist:
            return None

