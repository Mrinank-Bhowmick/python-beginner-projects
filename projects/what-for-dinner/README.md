# What For Dinner

A console app that suggests a random meal for dinner. It fetches a random recipe from TheMealDB API and prints the meal name, origin, category, cooking instructions, and a YouTube link in a colorized format.

## Example

```text
-------------------------------------------------------------
Let's have a Beef Rendang for dinner!
This menu is Malaysian and it is Beef!
You can follow this link: https://www.youtube.com/watch?v=... or the instructions to cook it:
Combine the spice paste with coconut milk and beef...
-------------------------------------------------------------
```

A different random meal is suggested on every run.

## How to run on localhost

```bash
pip install requests
python main.py
```

## Dependencies

- requests
