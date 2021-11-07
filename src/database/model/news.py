import uuid
from datetime import datetime
import mongoengine as mongo


class News(mongo.Document):

    id = mongo.UUIDField(primary_key=True, default=uuid.uuid4)
    title = mongo.StringField(required=True)
    text = mongo.StringField(required=True)
    author = mongo.StringField(required=True)
    created = mongo.DateTimeField(required=True, default=datetime.utcnow())
    edited = mongo.DateTimeField()

