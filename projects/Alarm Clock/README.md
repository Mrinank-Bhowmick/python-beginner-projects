# Alarm Clock

A Tkinter desktop alarm clock. Pick an hour, minute and second from the
drop-downs, press **Set Alarm**, and when the system clock reaches that time it
plays `sound.wav` on a loop until you press **Stop Alarm**.

The folder also contains `clock.py`, a standalone digital clock that shows the
current time and greets you based on the time of day.

## How to run

```bash
pip install pygame
python alarm_clock.py    # the alarm
python clock.py          # the digital clock
```

## Dependencies

- `tkinter` — GUI (ships with the standard Python installer)
- `pygame` — plays the alarm sound (`alarm_clock.py` only)

## Pyodide-runnable

No. Both scripts use a Tkinter window, and the alarm also uses `pygame` audio
and background threads — none of which work in the in-browser Pyodide playground.
