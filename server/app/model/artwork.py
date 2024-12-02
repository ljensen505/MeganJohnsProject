from typing import Optional, Type

from pydantic import HttpUrl

from app.constants import ART_MEDIUM_TABLE, ARTWORK_TABLE
from app.model.model_object import ModelObject
from app.model.response_object import ResponseObject


class Medium(ModelObject, ResponseObject):
    medium_name: str


class Artwork(ModelObject, ResponseObject):
    artwork_name: str
    source: HttpUrl
    thumbnail: HttpUrl
    is_featured: bool = False
    medium: Optional[Medium] = None
    release_year: Optional[int] = None
    size: Optional[str] = None

    @classmethod
    def select_one(
        cls, artwork_id: int, table_name: str = ARTWORK_TABLE
    ) -> "Artwork | None":
        cursor, conn = cls._get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT 
                a.id,
                a.medium_id ,
                a.artwork_name ,
                a.source ,
                a.thumbnail ,
                a.is_featured ,
                a.release_year ,
                a.`size` ,
                m.id as medium_id,
                m.medium_name
            FROM {table_name} a
            LEFT JOIN {ART_MEDIUM_TABLE} m ON a.medium_id = m.id
            WHERE a.id = {artwork_id}
            """
        )
        row: dict = cursor.fetchone()  # type: ignore
        cls._close_cursor_and_conn(cursor, conn)
        return cls._construct(cls, row) if row else None

    @classmethod
    def select_all(cls, table_name: str = ARTWORK_TABLE) -> list["Artwork"]:
        cursor, conn = cls._get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT 
                a.id,
                a.medium_id ,
                a.artwork_name ,
                a.source ,
                a.thumbnail ,
                a.is_featured ,
                a.release_year ,
                a.`size` ,
                m.id as medium_id,
                m.medium_name
            FROM {table_name} a
            LEFT JOIN {ART_MEDIUM_TABLE} m ON a.medium_id = m.id
            """
        )
        rows: list[dict] = cursor.fetchall()  # type: ignore
        cls._close_cursor_and_conn(cursor, conn)
        return sorted(
            [cls._construct(cls, row) for row in rows],
            key=lambda a: (a.is_featured, a.release_year if a.release_year else 0),
            reverse=True,
        )

    @classmethod
    def _construct(cls, Obj: Type, row: dict) -> "Artwork":
        row["medium"] = (
            Medium(id=row["medium_id"], medium_name=row["medium_name"])
            if row.get("medium_id")
            else None
        )
        return Obj(**row)
