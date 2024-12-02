from typing import Optional

from pydantic import BaseModel


class ResponseObject(BaseModel):
    id: Optional[int] = None
