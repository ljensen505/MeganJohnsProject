from typing import Optional, Type

from icecream import ic
from pydantic import HttpUrl

from app.constants import ALBUMS_TABLE, ARTISTS_TABLE
from app.model.model_object import ModelObject
from app.model.response_object import ResponseObject


class Artist(ModelObject, ResponseObject):
    artist_name: str
    artist_url: Optional[HttpUrl] = None


class Album(ModelObject, ResponseObject):
    album_name: str
    release_year: int
    artist: Artist
    front_artwork_url: HttpUrl
    spotify_url: Optional[HttpUrl] = None
    itunes_url: Optional[HttpUrl] = None
    bandcamp_url: Optional[HttpUrl] = None
    apple_music_url: Optional[HttpUrl] = None
    rear_artwork_url: Optional[HttpUrl] = None
    bandcamp_player: Optional[str] = None

    @classmethod
    def select_one(
        cls, album_id: int, table_name: str = ALBUMS_TABLE
    ) -> "Album | None":
        cursor, conn = cls._get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT
                	al.id,
                    al.album_name ,
                    al.release_year,
                    al.artist_id ,
                    al.spotify_url ,
                    al.itunes_url ,
                    al.bandcamp_url ,
                    al.apple_music_url ,
                    al.front_artwork_url ,
                    al.rear_artwork_url ,
                    al.bandcamp_player ,
                    ar.artist_name ,
                    ar.artist_url
            FROM {table_name} al
            LEFT JOIN {ARTISTS_TABLE} ar
            ON al.artist_id = ar.id
            WHERE al.id = {album_id};
            """
        )
        data: dict = cursor.fetchone()  # type: ignore
        cls._close_cursor_and_conn(cursor, conn)
        return cls._construct(cls, data) if data else None

    @classmethod
    def select_all(cls, table_name: str = ALBUMS_TABLE) -> list["Album"]:
        cursor, conn = cls._get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT
                	al.id,
                    al.album_name ,
                    al.release_year,
                    al.artist_id ,
                    al.spotify_url ,
                    al.itunes_url ,
                    al.bandcamp_url ,
                    al.apple_music_url ,
                    al.front_artwork_url ,
                    al.rear_artwork_url ,
                    al.bandcamp_player ,
                    ar.artist_name ,
                    ar.artist_url
            FROM {table_name} al
            LEFT JOIN {ARTISTS_TABLE} ar
            ON al.artist_id = ar.id;
            """
        )
        data: dict = cursor.fetchall()  # type: ignore
        cls._close_cursor_and_conn(cursor, conn)
        return sorted(
            [cls._construct(cls, row) for row in data],
            key=lambda album: album.release_year,
            reverse=True,
        )

    @classmethod
    def _construct(cls, Obj: Type, data: dict) -> "Album":
        data["artist"] = Artist(**data)
        return Obj(**data)
