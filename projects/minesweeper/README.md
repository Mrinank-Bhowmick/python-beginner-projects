# Minesweeper

A console version of the classic Minesweeper game. It builds a board, randomly plants bombs, and asks the player where to dig (entered as `row,col`). Digging an empty cell recursively reveals neighbouring cells; hitting a bomb ends the game.

## Example

```text
   0  1  2  3  4  5  6  7  8  9
----------------------------------
0 |  |  |  |  |  |  |  |  |  |  |
1 |  |  |  |  |  |  |  |  |  |  |
...
Where would you like to dig? Input as row,col: 3,5
   0  1  2  3  4  5  6  7  8  9
----------------------------------
0 |  |  |  |  |  |  |  |  |  |  |
...
3 |  |  |  |  |  |2 |  |  |  |  |
Where would you like to dig? Input as row,col: 0,0
SORRY GAME OVER :(
```

## How to run on localhost

```
python main.py
```

## Dependencies

Standard library only (`random`, `re`).
