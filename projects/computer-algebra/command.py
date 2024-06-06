from typing import Any
from abc import abstractmethod, ABC
from urllib.parse import quote


class CmdBase(ABC):
    """Base class for all the CAS (Computer Algebra System) API Commands."""

    def __init__(self, operation: str, base_url: str):
        self.operation = operation
        self.base_url = base_url

    @abstractmethod
    def command(self, expr: str) -> Any:
        """
        Command for sending request to Newton CAS API with a given expression string and returns the result from
        the API response.
        """
        pass

    @staticmethod
    def url_encode(inp_str: str) -> str:
        """Encode the input string to a URL-safe format."""
        return quote(inp_str)
