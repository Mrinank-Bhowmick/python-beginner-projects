from dataclasses import dataclass

import requests
from command import CmdBase


@dataclass(frozen=True)
class NewtonResponse:
    """Newton API Response."""

    operation: str
    expression: str
    result: str


class NewtonCmdException(Exception):
    """Base class for Newton Command Exceptions."""


class NewtonCommand(CmdBase):
    """Base class for all the Newton API Commands."""

    def __init__(self, operation: str):
        super().__init__(operation, "https://newton.now.sh/api/v2")

    def command(self, expr: str) -> NewtonResponse:
        """
        Command method for NewtonCommand class.

        Args:
            expr (str): Mathematical expression to be evaluated.

        Returns:
            NewtonResponse: Object containing the operation, expression, and result of the evaluated expression.

        Raises:
            NewtonCmdException: If the HTTP request fails or returns a non-success status code, the exception is raised
            with the error message.
        """
        # Construct the Request URL
        expr_encode = self.url_encode(expr)  # URL Encode for Expression
        request_url = f"{self.base_url}/{self.operation}/{expr_encode}"

        # Make the HTTP GET request
        response = requests.get(request_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Deserialize the JSON response into a dictionary
            response_data = response.json()

            # Extract relevant data from the response
            operation = response_data["operation"]
            expression = response_data["expression"]
            result = response_data["result"]

            # Create and return a NewtonResponse object
            return NewtonResponse(
                operation=operation, expression=expression, result=result
            )
        else:
            raise NewtonCmdException(f"{response.text}")


newton_simplify = NewtonCommand("simplify").command
newton_factor = NewtonCommand("factor").command
newton_derive = NewtonCommand("derive").command
newton_integrate = NewtonCommand("integrate").command
newton_zeroes = NewtonCommand("zeroes").command
newton_tangent = NewtonCommand("tangent").command
newton_area = NewtonCommand("area").command
newton_cos = NewtonCommand("cos").command
newton_sin = NewtonCommand("sin").command
newton_tan = NewtonCommand("tan").command
newton_arc_cos = NewtonCommand("arccos").command
newton_arc_sin = NewtonCommand("arcsin").command
newton_arc_tan = NewtonCommand("arctan").command
newton_abs = NewtonCommand("abs").command
newton_log = NewtonCommand("log").command

NEWTON_CMDS_DICT = {
    "simplify": newton_simplify,
    "factor": newton_factor,
    "derive": newton_derive,
    "integrate": newton_integrate,
    "zeroes": newton_zeroes,
    "tangent": newton_tangent,
    "area": newton_area,
    "cos": newton_cos,
    "sin": newton_sin,
    "tan": newton_tan,
    "arccos": newton_arc_cos,
    "arcsin": newton_arc_sin,
    "arctan": newton_arc_tan,
    "abs": newton_abs,
    "log": newton_log,
}
