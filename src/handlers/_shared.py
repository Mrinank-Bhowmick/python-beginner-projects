import json

from js import Object, Response
from pyodide.ffi import to_js


CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
}


def _opts(d):
    return to_js(d, dict_converter=Object.fromEntries)


def json_response(payload, status=200):
    body = json.dumps(payload)
    return Response.new(body, _opts({
        "status": status,
        "headers": {"Content-Type": "application/json; charset=utf-8", **CORS_HEADERS},
    }))


def error_response(message, status=400):
    return json_response({"error": message}, status=status)


def cors_preflight():
    return Response.new("", _opts({"status": 204, "headers": CORS_HEADERS}))


async def read_json(request):
    try:
        return (await request.json()).to_py()
    except Exception:
        return None
