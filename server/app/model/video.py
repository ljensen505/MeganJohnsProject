from typing import Optional, Type

from pydantic import HttpUrl

from app.constants import VIDEOS_TABLE
from app.model.model_object import ModelObject
from app.model.response_object import ResponseObject


class Video(ModelObject, ResponseObject):
    title: str
    subtitle: str
    description: str  # html
    source: HttpUrl
    embedded_player_iframe: str  # an iframe from YouTube/Vimeo
    website: Optional[HttpUrl] = None

    @classmethod
    def select_one(cls, obj_id: int, table_name: str = VIDEOS_TABLE) -> "Video | None":
        data = super().select_one(obj_id, table_name)
        return cls._construct(cls, data)

    @classmethod
    def select_all(cls, table_name: str = VIDEOS_TABLE) -> list["Video"]:
        return [cls._construct(cls, row) for row in super().select_all(table_name)]
