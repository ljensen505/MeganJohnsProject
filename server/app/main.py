from asyncio import gather

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.controller import controller
from app.model.albums import Album
from app.model.artwork import Artwork
from app.model.bio import Bio, ProfessionalService
from app.model.quotes import Quote
from app.model.video import Video
from app.routers.albums import router as albums_router
from app.routers.artwork import router as artwork_router
from app.routers.bio import router as bio_router
from app.routers.quotes import router as quotes_router
from app.routers.videos import router as videos_router

from .origins import origins

app = FastAPI()

app.include_router(albums_router)
app.include_router(artwork_router)
app.include_router(bio_router)
app.include_router(quotes_router)
app.include_router(videos_router)

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MeganJohns(BaseModel):
    albums: list[Album]
    artwork: list[Artwork]
    quotes: list[Quote]
    videos: list[Video]
    bio: Bio
    professional_services: list[ProfessionalService]


@app.get("/")
async def root() -> MeganJohns:
    albums, artwork, bio, quotes, videos, services = await gather(
        controller.get_all_albums(),
        controller.get_all_artwork(),
        controller.get_bio(),
        controller.get_all_quotes(),
        controller.get_all_videos(),
        controller.get_all_professional_services(),
    )
    return MeganJohns(
        albums=albums,
        artwork=artwork,
        quotes=quotes,
        videos=videos,
        bio=bio,
        professional_services=services,
    )
