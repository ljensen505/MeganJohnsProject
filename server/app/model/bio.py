from pydantic import HttpUrl

from app.constants import BIO_CONTENT_TABLE, SERVICES_TABLE, SOCIAL_TABLE
from app.model.model_object import ModelObject
from app.model.response_object import ResponseObject


class ProfessionalService(ModelObject, ResponseObject):
    service_name: str

    @classmethod
    def select_all(
        cls, table_name: str = SERVICES_TABLE
    ) -> list["ProfessionalService"]:
        return [
            cls._construct(ProfessionalService, row)
            for row in super().select_all(table_name)
        ]

    @classmethod
    def select_one(
        cls, obj_id: int, table_name: str = SERVICES_TABLE
    ) -> "ProfessionalService | None":
        return cls._construct(
            ProfessionalService, super().select_one(obj_id, table_name)
        )


class SocialUrl(ModelObject, ResponseObject):
    social_name: str
    social_url: HttpUrl

    @classmethod
    def select_one(
        cls, obj_id: int, table_name: str = SOCIAL_TABLE
    ) -> "SocialUrl | None":
        return cls._construct(SocialUrl, super().select_one(obj_id, table_name))

    @classmethod
    def select_all(cls, table_name: str = SOCIAL_TABLE) -> list["SocialUrl"]:
        return [
            cls._construct(SocialUrl, row) for row in super().select_all(table_name)
        ]


class Bio(ModelObject, ResponseObject):
    name: str
    bio: str
    social_urls: list[SocialUrl]

    @classmethod
    def select_one(cls, table_name: str = BIO_CONTENT_TABLE) -> "Bio":
        bio_data = super().select_one(1, table_name)
        bio_content = bio_data.get("content", "") if bio_data else ""
        socials = SocialUrl.select_all()
        bio = Bio(bio=bio_content, social_urls=socials, name="Megan Johns")
        del bio.id
        return bio

    @classmethod
    def select_all(cls, **args) -> None:
        raise NotImplemented
