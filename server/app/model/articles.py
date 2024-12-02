from typing import Optional

from pydantic import BaseModel, HttpUrl


class Article(BaseModel):
    id: int
    article_title: str
    body: str
    is_featured: Optional[bool] = False
    video_url: Optional[HttpUrl] = None
