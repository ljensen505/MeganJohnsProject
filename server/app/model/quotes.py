from typing import Optional, Type

from icecream import ic
from pydantic import HttpUrl

from app.constants import QUOTES_TABLE
from app.model.model_object import ModelObject
from app.model.response_object import ResponseObject


class Quote(ModelObject, ResponseObject):
    body: str
    author: str
    source: Optional[HttpUrl] = None

    @classmethod
    def select_one(cls, obj_id: int, table_name: str = QUOTES_TABLE) -> "Quote | None":
        return cls._construct(cls, super().select_one(obj_id, table_name))

    @classmethod
    def select_all(cls, table_name: str = QUOTES_TABLE) -> list["Quote"]:
        return [cls._construct(cls, row) for row in super().select_all(table_name)]
