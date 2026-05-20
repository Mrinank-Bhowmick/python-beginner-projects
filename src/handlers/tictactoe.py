import random

from ._shared import error_response, json_response, read_json


WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def winner_on(board):
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return all(cell for cell in board)


def free_squares(board, options):
    return [i for i in options if not board[i]]


def computer_move(board, cpu_letter):
    player_letter = "O" if cpu_letter == "X" else "X"

    # 1. win if possible
    for i in range(9):
        if not board[i]:
            board[i] = cpu_letter
            if winner_on(board) == cpu_letter:
                board[i] = ""
                return i
            board[i] = ""

    # 2. block opponent
    for i in range(9):
        if not board[i]:
            board[i] = player_letter
            if winner_on(board) == player_letter:
                board[i] = ""
                return i
            board[i] = ""

    # 3. corner, center, side
    for group in ([0, 2, 6, 8], [4], [1, 3, 5, 7]):
        free = free_squares(board, group)
        if free:
            return random.choice(free)
    return None


async def handle(request, env):
    body = await read_json(request)
    if body is None:
        return error_response("invalid JSON")

    board = body.get("board")
    player = body.get("player")
    move = body.get("move")

    if (not isinstance(board, list) or len(board) != 9
            or not all(c in ("", "X", "O") for c in board)):
        return error_response("board must be 9-array of '', 'X', or 'O'")
    if player not in ("X", "O"):
        return error_response("player must be 'X' or 'O'")
    if move is not None:
        if not isinstance(move, int) or not (0 <= move < 9):
            return error_response("move must be int 0..8")
        if board[move]:
            return error_response("square already taken")
        board[move] = player

    win = winner_on(board)
    if win:
        return json_response({"board": board, "status": "win", "winner": win})
    if is_full(board):
        return json_response({"board": board, "status": "draw"})

    cpu_letter = "O" if player == "X" else "X"
    cpu_idx = computer_move(board, cpu_letter)
    if cpu_idx is not None:
        board[cpu_idx] = cpu_letter

    win = winner_on(board)
    if win:
        return json_response({"board": board, "status": "win", "winner": win, "cpu_move": cpu_idx})
    if is_full(board):
        return json_response({"board": board, "status": "draw", "cpu_move": cpu_idx})

    return json_response({"board": board, "status": "ongoing", "cpu_move": cpu_idx})
