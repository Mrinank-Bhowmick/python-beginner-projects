# Minecraft in Python

A simple Minecraft-style voxel sandbox built with the `ursina` 3D game engine. You can walk around in first-person, place and break blocks of several textures, and switch block types with the number keys.

## Example

1. Run the script — a 3D first-person window opens showing a 20×20 flat terrain of grass blocks with a sky sphere.
2. Use W/A/S/D to walk and the mouse to look around.
3. Left-click a block to place a new block of the currently selected type adjacent to it (a punch sound plays).
4. Right-click a block to remove it.
5. Press keys 1–4 to switch the active block texture: 1 = grass, 2 = stone, 3 = brick, 4 = dirt.

## How to run on localhost

```
pip install ursina
python "Minecraft-in-Python-main/UrsaCraft_video.py"
```

(`ursina_intro.py` is a smaller introductory example.)

## Dependencies

- ursina
