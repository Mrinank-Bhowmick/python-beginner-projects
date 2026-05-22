# Type Racer Game

A typing-speed game built with Tkinter. A random sentence appears and you type it against a countdown timer, with live progress, color feedback for correct/incorrect text, and a words-per-minute score.

## Example

1. The window opens titled "TypeRacer" (800×400). A random sentence appears, e.g. `Python is an interpreted high-level programming language`.
2. A 5-second countdown ("Get ready!", 5, 4, 3, 2, 1, "Go!") plays, then the 30-second game timer starts.
3. You type in the entry box. Correct characters turn the text green; any mismatch turns it red. The progress bar updates as you type.
4. If you finish the sentence before time runs out, the result label briefly shows `Correct! Time taken: 18.42 seconds, WPM: 52` and a new sentence is loaded automatically.
5. If the timer reaches zero, it shows `Time's up!` and the score is submitted.

## How to run on localhost

```bash
python type_racer.py
```

## Dependencies

Standard library only (`tkinter`, `random`, `time`).
