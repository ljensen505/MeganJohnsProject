from fastapi import APIRouter

from app.controller import controller
from app.model import Video

router = APIRouter(
    prefix="/videos",
    tags=["videos"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def all_videos() -> list[Video]:
    return await controller.get_all_videos()


@router.get("/{video_id}")
async def video(video_id: int) -> Video:
    return controller.get_one_video(video_id)
