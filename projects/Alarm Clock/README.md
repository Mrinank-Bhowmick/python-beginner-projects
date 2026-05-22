# Alarm Clock

A Tkinter desktop alarm clock. Pick an hour, minute and second from the
drop-downs, press **Set Alarm**, and when the system clock reaches that time it
plays `sound.wav` on a loop until you press **Stop Alarm**.

The folder also contains `clock.py`, a standalone digital clock that shows the
current time and greets you based on the time of day.

## Example

1. The window opens showing three drop-down menus labelled with hours, minutes,
   and seconds, along with **Set Alarm** and **Stop Alarm** buttons.
2. Select `07`, `30`, `00` from the drop-downs to set an alarm for 07:30:00.
3. Click **Set Alarm**. The program checks the system clock once per second in
   the background, printing `07:29:55 07:30:00` to the console each tick.
4. When the system clock reaches `07:30:00`, `sound.wav` starts playing on a
   loop and "Wake Up now!" is printed to the console.
5. Click **Stop Alarm** to stop the sound.

## How to run on localhost

```bash
pip install pygame
python alarm_clock.py    # the alarm
python clock.py          # the digital clock
```

## Dependencies

- `tkinter` — GUI (ships with the standard Python installer)
- `pygame` — plays the alarm sound (`alarm_clock.py` only)
