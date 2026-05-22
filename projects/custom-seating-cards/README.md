# Custom Seating Cards

Creates a decorative PNG seating/place card for each guest listed in `guests.txt`, drawing their name over a flower image with a custom font.

## Example

Given a `guests.txt` containing:
```
Alice
Bob
```

Running the script creates an `imageCards/` folder containing:
- `Alice_card.png` — a 291x363 PNG with the flower background and "Alice" drawn in red using the Pacifico font.
- `Bob_card.png` — the same layout with "Bob".

## How to run on localhost

```
pip install Pillow
python custom_cards.py
```

## Dependencies

- `Pillow` (`PIL`)
