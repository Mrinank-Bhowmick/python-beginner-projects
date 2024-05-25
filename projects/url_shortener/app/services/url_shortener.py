from configparser import ParsingError
from typing import Optional, Union

import pyshorteners
from pydantic import BaseModel, PrivateAttr, ValidationError


class URLShortener(BaseModel):
    url: str
    _shortener: Optional[pyshorteners.Shortener] = PrivateAttr()

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        """
        Initialize the URLShortener. If no 'shortener' is provided in data,
        a new pyshorteners.Shortener instance is created.
        """
        shortener = data.pop("shortener", None) or pyshorteners.Shortener()
        super().__init__(**data)
        self._shortener = shortener

    def shorten_url(self) -> Union[str, Exception]:
        if self._shortener is None:
            raise ValueError("Shortener is not initialized.")

        try:
            return str(self._shortener.tinyurl.short(self.url))
        except (ParsingError, ValidationError) as error:
            return error
        except Exception as generic_error:
            return generic_error
