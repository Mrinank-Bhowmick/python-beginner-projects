# Mouse Activity Script

This Python script periodically moves the mouse and performs a click action. It’s useful for keeping the system active to avoid timeouts or showing as idle in applications like Microsoft Teams.

## Example

1. Run `python AutoGui.py`. The script runs silently in the background.
2. Every 20 seconds the mouse moves 100 pixels diagonally and then returns to
   its original position, followed by a click.
3. This keeps the system active and prevents idle status in applications such
   as Microsoft Teams.
4. Press **Ctrl+C** in the terminal to stop the script. The console prints:
   ```text
   Script terminated by user
   ```

## Features
- Moves the mouse slightly every 20 seconds
- Simulates a mouse click periodically
- Prevents idle status on Microsoft Teams
