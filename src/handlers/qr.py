import base64
import io

import qrcode

from ._shared import error_response, json_response, read_json


async def handle(request, env):
    body = await read_json(request)
    if body is None:
        return error_response("invalid JSON")
    text = (body.get("text") or "").strip()
    if not text:
        return error_response("text required")
    if len(text) > 1024:
        return error_response("text too long (max 1024 chars)")

    q = qrcode.QRCode(version=1, box_size=10, border=4)
    q.add_data(text)
    q.make(fit=True)
    img = q.make_image(fill_color="black", back_color="white")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    png_b64 = base64.b64encode(buf.getvalue()).decode("ascii")

    return json_response({"png_b64": png_b64})
