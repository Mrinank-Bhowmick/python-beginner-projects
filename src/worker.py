from urllib.parse import urlparse

from handlers import bmi, hangman, madlibs, qr, rps, tictactoe
from handlers._shared import cors_preflight, error_response


ROUTES = {
    "/api/bmi": bmi.handle,
    "/api/rps": rps.handle,
    "/api/qr": qr.handle,
    "/api/madlibs": madlibs.handle,
    "/api/tictactoe": tictactoe.handle,
    "/api/hangman": hangman.handle,
}


async def on_fetch(request, env):
    path = urlparse(request.url).path

    if path in ROUTES:
        if request.method == "OPTIONS":
            return cors_preflight()
        if request.method != "POST":
            return error_response("POST only", 405)
        return await ROUTES[path](request, env)

    return error_response("not found", 404)
