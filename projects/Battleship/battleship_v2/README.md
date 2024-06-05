# Battleship 2.0

## Description

Modular Battleship Game. This application is an attempt to modularize the
first implementation of the Battleship game
by [Robert Lent](https://github.com/ca20110820/python-beginner-projects/tree/spike/battleship/projects/Battleship).

## Requirements and Installation

- Python >= 3.9+

Clone the original
repository [Mrinank-Bhowmick/python-beginner-projects](https://github.com/Mrinank-Bhowmick/python-beginner-projects)
to your local machine and go to the directory `projects/Battleship/battleship_v2/`. From here, you can extend this
application, write your scripts own with the components, or play the game on the command-line.

## Features

- Closely Resembles the Battleship Boardgame
- Modular
- Extendable for GUI
- CLI Game
- Random Bot Player
- Supports 2 Players

## Usage

### CLI

To play the command-line Battleship, simply run:

```bash
python game.py
```

The game would prompt the user for:

- Board Size (`5 <= board_size <= 15`)
- Player 1's Name
- Play with a Random Bot or Not
- Player 2' Name

The CLI Game would display 2 boards: Your _Hit or Miss_ on the Enemy Board when you attack:

- `X` - _Hit_
- `O` - _Missed_
- `-` - _No Attack_

and the status of your board when the enemy attacks:

- `S` - _Ship_
- `H` - _Hit_
- `M` - _Missed_
- `-` - _No Attack_

When entering an attack coordinate, simply enter the row and column indexes separated
by space.
For example:

```text
Please Enter the Attack Coordinates Admiral P1 >>> 0 4
```

would attack the coordinate `(0, 4)`. This is different from the first
Battleship implementation where the index starts at 1. This version starts at `0`.

The board would print the valid indexes:
```text
    0   1   2   3   4
 0  - | - | - | - | - 
 1  - | - | - | - | - 
 2  - | - | - | - | - 
 3  - | - | - | - | - 
 4  - | - | - | - | - 
```

<details>
<summary><b>Sneak peek - CLI</b></summary>

```
Enter Board Size >>> 5
Please Enter the Name for Player 1 >>> P1
Do you want to play with a bot? (yes/no) >>> yes
Please Enter the Name for Player 2 >>> Bot
Randomly placing ship ...
Player Bot moves first.
Bot (Bot) is attacking on (0, 0) ...


Please Enter the Attack Coordinates Admiral P1 >>> 1 5
Attack Coordinates must be in [0, 5)
Invalid Attack Coordinate
Please Enter the Attack Coordinates Admiral P1 >>> 1 1
P1 Battlefield Situation
    0   1   2   3   4
 0  H | - | S | - | S 
 1  S | - | S | S | S 
 2  S | - | S | S | S 
 3  S | S | S | - | - 
 4  - | - | S | - | - 

P1 Targets
    0   1   2   3   4
 0  - | - | - | - | - 
 1  - | O | - | - | - 
 2  - | - | - | - | - 
 3  - | - | - | - | - 
 4  - | - | - | - | - 


Bot (Bot) is attacking on (0, 1) ...


Please Enter the Attack Coordinates Admiral P1 >>> asd asd
Invalid Attack Coordinate
Please Enter the Attack Coordinates Admiral P1 >>> 4 4
P1 Battlefield Situation
    0   1   2   3   4
 0  H | M | S | - | S 
 1  S | - | S | S | S 
 2  S | - | S | S | S 
 3  S | S | S | - | - 
 4  - | - | S | - | - 

P1 Targets
    0   1   2   3   4
 0  - | - | - | - | - 
 1  - | O | - | - | - 
 2  - | - | - | - | - 
 3  - | - | - | - | - 
 4  - | - | - | - | O 


Bot (Bot) is attacking on (2, 4) ...


Please Enter the Attack Coordinates Admiral P1 >>> 0 4
P1 Battlefield Situation
    0   1   2   3   4
 0  H | M | S | - | S 
 1  S | - | S | S | S 
 2  S | - | S | S | H 
 3  S | S | S | - | - 
 4  - | - | S | - | - 

P1 Targets
    0   1   2   3   4
 0  - | - | - | - | X 
 1  - | O | - | - | - 
 2  - | - | - | - | - 
 3  - | - | - | - | - 
 4  - | - | - | - | O 


Bot (Bot) is attacking on (4, 0) ...


Please Enter the Attack Coordinates Admiral P1 >>> 3 3
P1 Battlefield Situation
    0   1   2   3   4
 0  H | M | S | - | S 
 1  S | - | S | S | S 
 2  S | - | S | S | H 
 3  S | S | S | - | - 
 4  M | - | S | - | - 

P1 Targets
    0   1   2   3   4
 0  - | - | - | - | X 
 1  - | O | - | - | - 
 2  - | - | - | - | - 
 3  - | - | - | X | - 
 4  - | - | - | - | O 


Bot (Bot) is attacking on (1, 4) ...


Please Enter the Attack Coordinates Admiral P1 >>> 
```

</details>

## Developer

[ca20110820](https://github.com/ca20110820)