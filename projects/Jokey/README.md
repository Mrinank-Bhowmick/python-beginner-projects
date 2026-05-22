# Jokey

A console joke teller that fetches jokes from the JokeAPI, with settings to change joke category and language.

## Example

```text
Do you want to read a joke?(y => yes; n => exit; s=> settings): y

Why do Java developers wear glasses? Because they don't C#.
...

Do you want to read a joke?(y => yes; n => exit; s=> settings): s
Which settings would you like to edit? (c => category, l => language): c
Current selected category: Any

Selectable categories:
 a => Any
 p => Programming
 m => Misc
 d => dark
 s => Spooky
 c => Christmas
 > p
Category Programming set!

Do you want to read a joke?(y => yes; n => exit; s=> settings): n
```

## How to run on localhost

```
pip install requests
python joketeller.py
```

## Dependencies

requests.
