from ._shared import error_response, json_response, read_json


def generate_madlib(choice, adjective, noun, verb, adverb):
    stories = {
        1: (
            f"In a mystical and distant land, there was a brave and {adjective} explorer named {noun}. "
            f"{noun.capitalize()} had always dreamed of {verb} {adverb} to discover hidden treasures. "
            f"One day, while {verb} {adverb} deep in the dense {adjective} jungle, {noun} stumbled upon an ancient {noun}. "
            f"The {noun} was covered in {adjective} vines and moss, but it {verb} {adverb} with the promise of untold riches. "
            f"With {adjective} excitement, {noun} began to {verb} {adverb}, clearing away every obstacle. "
            f"At the heart of the {noun}, a {adjective} light {verb} {adverb}, revealing a chest of {adjective} {noun}. "
            f"{noun} decided to {verb} {adverb} home and share the {adjective} riches with the village — "
            f"and lived {adverb} ever after."
        ),
        2: (
            f"In the enchanting world of {noun}, there existed a {adjective} school known as the {adjective} Academy of {noun}. "
            f"Our protagonist, {noun}, had always dreamed of {verb} {adverb} and becoming a {adjective} wizard. "
            f"At the academy, {noun} learned to {verb} {adverb}, brew {adjective} potions, and cast {adjective} spells. "
            f"With a {adjective} friend by their side, {noun} set out to {verb} {adverb} and uncover the secrets of the {adjective} forest, "
            f"making the world a {adjective} place along the way."
        ),
        3: (
            f"In the bustling city of {noun}, Dr. {noun} was renowned for {verb} {adverb} and pushing the boundaries of {adjective} science. "
            f"One day, Dr. {noun} had a {adjective} idea: a {adjective} time machine. "
            f"After many {adjective} experiments, Dr. {noun} stepped inside and {verb} {adverb} into the unknown. "
            f"In a {adjective} era, Dr. {noun} encountered {adjective} figures and had the chance to {verb} {adverb} with legends — "
            f"only to return with a {adjective} new appreciation for the {adjective} present."
        ),
    }
    return stories.get(choice)


async def handle(request, env):
    body = await read_json(request)
    if body is None:
        return error_response("invalid JSON")

    try:
        choice = int(body.get("story", 1))
    except (TypeError, ValueError):
        return error_response("story must be 1, 2, or 3")
    if choice not in (1, 2, 3):
        return error_response("story must be 1, 2, or 3")

    def field(key):
        v = body.get(key)
        if not isinstance(v, str) or not v.strip():
            return None
        return v.strip()[:40]

    adjective = field("adjective")
    noun = field("noun")
    verb = field("verb")
    adverb = field("adverb")
    if not all([adjective, noun, verb, adverb]):
        return error_response("adjective, noun, verb, adverb required")

    story = generate_madlib(choice, adjective, noun, verb, adverb)
    return json_response({"story": story})
