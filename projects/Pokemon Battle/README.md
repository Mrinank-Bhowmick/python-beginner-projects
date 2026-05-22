# Pokemon Battle

A turn-based Pokemon battle game in the console. Two Pokemon (with types, moves, attack and defense stats) fight each other; type advantages affect damage, health bars update each turn, and text is printed one character at a time for effect.

## Example

```text
-----POKEMONE BATTLE-----

Blastoise
TYPE/ Water
ATTACK/ 10
DEFENSE/ 10
LVL/ 33.0

VS

Squirtle
TYPE/ Water
ATTACK/ 3
DEFENSE/ 3
LVL/ 12.0

Blastoise		HLTH	====================
Squirtle		HLTH	====================

Go Blastoise!
1. Water Gun
2. Bubblebeam
3. Hydro Pump
4. Surf
Pick a move: 3
Blastoise used Hydro Pump!
Its not very effective...

Blastoise		HLTH	====================
Squirtle		HLTH	==========

...Squirtle fainted.
Opponent paid you $2341.
```

## How to run on localhost

```
pip install numpy
python pokemon.py
```

## Dependencies

- numpy
