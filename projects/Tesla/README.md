# Tesla Self-Driving Car

A Pygame simulation of a self-driving car. A car follows a track image by sampling pixel colors ahead of it to decide when to drive straight or turn.

## Example

1. The Pygame window opens displaying the track image as a background.
2. The car sprite appears on the track and begins moving forward automatically.
3. As the car approaches a curve, it samples pixel colors ahead of it and steers left or right to stay on the light-colored road surface.
4. The car continues navigating the track autonomously with no user input required.
5. Close the window to exit the simulation.

## How to run on localhost

```
pip install pygame
python tesla.py
```

## Dependencies

pygame
