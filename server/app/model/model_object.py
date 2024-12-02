from typing import Any, Optional, Type

from icecream import ic
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from pydantic import BaseModel

from app.db.conn import connect_db


class ModelObject:
    @classmethod
    def select_one(cls, obj_id: int, table_name: str = "") -> dict | None:
        if not table_name:
            raise Exception(
                "table_name cannot be an empty string. Check default arguments."
            )
        cursor, conn = cls._get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT *
            FROM {table_name}
            WHERE id = {obj_id};
            """
        )
        data: dict[Any, Any] | None = cursor.fetchone()  # type: ignore
        cls._close_cursor_and_conn(cursor, conn)
        return data

    @classmethod
    def select_all(cls, table_name: str = "") -> list[dict]:
        if not table_name:
            raise Exception(
                "table_name cannot be an empty string. Check default arguments."
            )
        cursor, conn = cls._get_cursor_and_conn()
        cursor.execute(
            f"""-- sql
            SELECT *
            FROM {table_name};
            """
        )
        data: list[dict] = cursor.fetchall()  # type: ignore
        cls._close_cursor_and_conn(cursor, conn)
        return data

    @classmethod
    def _get_cursor_and_conn(cls) -> tuple[MySQLCursor, MySQLConnection]:
        conn = connect_db()
        return conn.cursor(dictionary=True), conn

    @classmethod
    def _close_cursor_and_conn(cls, cursor: MySQLCursor, conn: MySQLConnection) -> None:
        cursor.close()
        conn.close()

    @classmethod
    def _construct(cls, Obj: Type, data: dict | None) -> Any:
        return Obj(**data) if data is not None else None
