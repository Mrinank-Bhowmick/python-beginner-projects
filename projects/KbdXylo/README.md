# Keyboard Xylophone

Turns your keyboard into a xylophone by listening for key presses and playing a tone based on each key's character value.

## Example

1. Run `python main.py`. The program starts listening for key presses silently in the background.
2. Press any character key (e.g., `a`, `s`, `d`). Each key plays a tone whose frequency is the ASCII value of that character multiplied by 10 (e.g., pressing `a` plays 970 Hz, `s` plays 1150 Hz).
3. Each tone lasts 250 ms at a low volume.
4. Press Escape to stop the program.

## How to run on localhost

```
pip install -r requirements.txt
python main.py
```

## Dependencies

boombox, pynput.
