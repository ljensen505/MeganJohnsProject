from fastapi import APIRouter

from app.controller import controller
from app.model.bio import Bio, ProfessionalService

router = APIRouter(
    prefix="/bio",
    tags=["bio"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def bio() -> Bio:
    return await controller.get_bio()


@router.get("/services")
async def services() -> list[ProfessionalService]:
    return await controller.get_all_professional_services()
