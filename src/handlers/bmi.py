from ._shared import error_response, json_response, read_json


def calculate_bmi(height_m, weight_kg):
    return round(weight_kg / (height_m ** 2), 2)


def category_for(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 24.9:
        return "Normal weight"
    if bmi < 29.9:
        return "Overweight"
    if bmi < 34.9:
        return "Obese (Class I)"
    if bmi < 39.9:
        return "Obese (Class II)"
    return "Obese (Class III)"


async def handle(request, env):
    body = await read_json(request)
    if body is None:
        return error_response("invalid JSON")
    try:
        h = float(body["height_m"])
        w = float(body["weight_kg"])
    except (KeyError, TypeError, ValueError):
        return error_response("height_m and weight_kg required (numbers)")
    if h <= 0 or w <= 0:
        return error_response("height_m and weight_kg must be > 0")

    bmi = calculate_bmi(h, w)
    return json_response({"bmi": bmi, "category": category_for(bmi)})
