# Py-Battleship

  [![License](https://img.shields.io/static/v1?label=License&message=GPL-3-0&color=blue&?style=plastic&logo=appveyor)](https://opensource.org/license/GPL-3-0)

## Table Of Content

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [GitHub](#github)
- [License](#license)


![GitHub repo size](https://img.shields.io/github/repo-size/robertlent/py_battleship?style=plastic)

  ![GitHub top language](https://img.shields.io/github/languages/top/robertlent/py_battleship?style=plastic)



## Description

  Battleship is a Python command line game.

The player can choose the size of the grid, from 5x5 up to 15x15, and the ship will be randomly placed in that grid. The size of the grid also determines the number of turns the user gets, from 5 to 15.

The game handles incorrect entries and can be replayed repeatedly.



## Example

```text
Do you want to start a new game of Battleship? yes
Enter a number between 5 and 15.

This will determine how big the playing board is and how many turns you have to find the Battleship. (5 rows, 5 columns, 5 turns, etc.): 5
Welcome to Battleship.

A ship, one cell long, has been randomly placed on the below 5x5 grid.
You have 5 turns to find it.

O O O O O
O O O O O
O O O O O
O O O O O
O O O O O

Turn 1 of 5

Guess Row: 3
Guess Column: 2
Miss!

O O O O O
O O O O O
O O O O O
O O X O O
O O O O O

Turn 2 of 5

Guess Row: 1
Guess Column: 4
Congratulations! You sank my battleship!
```

## Installation

Download main.py, change to the directory where you downloaded the file and run it using `python3 main.py`

Py-Battleship is built with the following tools and libraries: <ul><li>Python</li></ul>



## Usage
 
1. Enter 'yes' or 'y' to start a new game
    - Any input besides those two and 'no' or 'n' will be ignored
2. You will be prompted to choose a number from 5 to 15, which sets the game board size and number of guesses to that number
3. You will be prompted to choose a row number and then to choose a column number
    - If either guess is less than 5 or more than the previously provided maximum, you will be prompted to choose a valid selection
    - If you enter a row or column that you already guessed, you will be told such and you will have used a turn
4. The game continues until you either make a correct guess or run out of guesses
5. You will then be asked if you want to start a new game


## GitHub

<a href="https://github.com/robertlent"><strong>robertlent</a></strong>


## License

[![License](https://img.shields.io/static/v1?label=Licence&message=GPL-3-0&color=blue)](https://opensource.org/license/GPL-3-0)
