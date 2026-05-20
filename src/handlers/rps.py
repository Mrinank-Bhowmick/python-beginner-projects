from random import randint

from ._shared import error_response, json_response, read_json


CHOICES = {1: "rock", 2: "paper", 3: "scissors"}
WIN_PAIRS = {"13", "21", "32"}  # player vs cpu where player wins


async def handle(request, env):
    body = await read_json(request)
    if body is None:
        return error_response("invalid JSON")

    choice = str(body.get("choice", "")).lower()
    player_num = next((k for k, v in CHOICES.items() if v == choice), None)
    if player_num is None:
        return error_response("choice must be rock|paper|scissors")

    cpu_num = randint(1, 3)
    if player_num == cpu_num:
        result = "draw"
    elif f"{player_num}{cpu_num}" in WIN_PAIRS:
        result = "win"
    else:
        result = "lose"

    return json_response({
        "player": CHOICES[player_num],
        "cpu": CHOICES[cpu_num],
        "result": result,
    })
