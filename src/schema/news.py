import datetime
import uuid
from pydantic import BaseModel
from typing import Optional


class NewsInsert(BaseModel):
    title: str
    text: str
    author: str


class NewsCustom(BaseModel):
    title: Optional[str]
    text: Optional[str]
    author: Optional[str]
    id: Optional[uuid.UUID]
    created: Optional[datetime.datetime]
    edited: Optional[datetime.datetime]


class NewsUpdate(BaseModel):
    title: Optional[str]
    text: Optional[str]
    author: Optional[str]



