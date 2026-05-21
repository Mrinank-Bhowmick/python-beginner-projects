# Keyboard Xylophone

Turns your keyboard into a xylophone by listening for key presses and playing a tone based on each key's character value.

## How to run

```
pip install -r requirements.txt
python main.py
```

## Dependencies

boombox, pynput.

## Pyodide-runnable
No — it uses pynput to capture global keyboard events and plays audio through the system sound device.
