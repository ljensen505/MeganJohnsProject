from pathlib import Path

from fastapi import status
from fastapi.exceptions import HTTPException
from git import Repo
from icecream import ic

from app.model import Album, Artwork, Bio, ProfessionalService, Quote, SocialUrl, Video


class Controller:
    def __init__(self) -> None:
        pass

    async def get_version(self) -> str:
        repo = Repo(Path.cwd().parent.joinpath(".git"))
        tags = [tag.tag for tag in repo.tags if tag.tag is not None]
        tags.sort(key=lambda t: t.tagged_date)
        return tags[-1].tag

    async def get_all_videos(self) -> list[Video]:
        return Video.select_all()

    def get_one_video(self, video_id: int) -> Video:
        if (video := Video.select_one(video_id)) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return video

    async def get_all_quotes(self) -> list[Quote]:
        return Quote.select_all()

    def get_one_quote(self, quote_id: int) -> Quote:
        if (quote := Quote.select_one(quote_id)) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return quote

    async def get_all_albums(self) -> list[Album]:
        return Album.select_all()

    def get_one_album(self, album_id: int) -> Album:
        if (album := Album.select_one(album_id)) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return album

    async def get_all_artwork(self) -> list[Artwork]:
        return Artwork.select_all()

    def get_one_artwork(self, artwork_id: int) -> Artwork:
        if (artwork := Artwork.select_one(artwork_id)) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return artwork

    async def get_bio(self) -> Bio:
        return Bio.select_one()

    async def get_all_professional_services(self) -> list[ProfessionalService]:
        return ProfessionalService.select_all()

    def get_one_professional_service(self, service_id) -> ProfessionalService:
        if (service := ProfessionalService.select_one(service_id)) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return service
