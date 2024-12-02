from fastapi import APIRouter

from app.controller import controller
from app.model import Artwork

router = APIRouter(
    prefix="/artwork",
    tags=["artwork"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all_artwork() -> list[Artwork]:
    return await controller.get_all_artwork()


@router.get("/{artwork_id}")
async def artwork(artwork_id: int) -> Artwork:
    return controller.get_one_artwork(artwork_id)
