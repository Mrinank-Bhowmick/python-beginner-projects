from pydantic import BaseModel, HttpUrl


class UrlShortenerValidation(BaseModel):
    url: HttpUrl
