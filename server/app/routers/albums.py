from fastapi import APIRouter

from app.controller import controller
from app.model import Album

router = APIRouter(
    prefix="/albums",
    tags=["albums"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all_albums() -> list[Album]:
    return await controller.get_all_albums()


@router.get("/{album_id}")
async def album(album_id: int) -> Album:
    return controller.get_one_album(album_id)
