import random

from ._shared import error_response, json_response, read_json


WORDS = {
    "easy": [
        "egg", "toy", "water", "day", "shower", "tiger", "home", "coat",
        "garden", "throw", "crown", "baby", "office", "beach", "phone",
        "computer", "flower", "bank", "train", "brush", "game",
    ],
    "medium": [
        "soup", "tree", "purple", "orange", "rocket", "pillow", "guitar",
        "kitchen", "window", "yellow", "planet", "doctor", "rabbit",
        "engine", "ticket", "candle", "puzzle", "mountain", "ocean",
    ],
    "hard": [
        "syzygy", "labyrinth", "quixotic", "ephemeral", "petrichor",
        "serendipity", "sonder", "limerence", "halcyon",
    ],
}

INITIAL_TRIES = {"easy": 8, "medium": 6, "hard": 4}


def pick_word(difficulty, seed):
    pool = WORDS.get(difficulty, WORDS["medium"])
    rng = random.Random(seed)
    return rng.choice(pool).upper()


def mask_word(word, guessed_letters):
    return "".join((c if c in guessed_letters else "_") for c in word)


async def handle(request, env):
    body = await read_json(request)
    if body is None:
        return error_response("invalid JSON")

    difficulty = (body.get("difficulty") or "medium").lower()
    if difficulty not in WORDS:
        return error_response("difficulty must be easy|medium|hard")

    seed = body.get("word_seed")
    if not isinstance(seed, int):
        return error_response("word_seed (int) required")

    guessed = body.get("guessed") or []
    if not isinstance(guessed, list) or not all(isinstance(g, str) and len(g) == 1 for g in guessed):
        return error_response("guessed must be a list of single letters")
    guessed_set = {g.upper() for g in guessed if g.isalpha()}

    word = pick_word(difficulty, seed)
    wrong = sorted(g for g in guessed_set if g not in word)
    max_tries = INITIAL_TRIES[difficulty]
    tries_left = max_tries - len(wrong)
    mask = mask_word(word, guessed_set)

    if "_" not in mask:
        status = "win"
    elif tries_left <= 0:
        status = "lose"
    else:
        status = "ongoing"

    out = {
        "mask": mask,
        "wrong": wrong,
        "tries_left": max(0, tries_left),
        "max_tries": max_tries,
        "status": status,
        "word_length": len(word),
    }
    if status == "lose":
        out["word"] = word

    return json_response(out)
