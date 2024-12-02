from fastapi import APIRouter

from app.controller import controller
from app.model import Quote

router = APIRouter(
    prefix="/quotes",
    tags=["quotes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all_quotes() -> list[Quote]:
    return await controller.get_all_quotes()


@router.get("/{id}")
async def quote(id: int) -> Quote:
    return controller.get_one_quote(id)
