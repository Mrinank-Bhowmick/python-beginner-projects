# Blender Tools with Unreal/Unity

## Description

A series of tools used to store vertex data in various ways. The data can then used in a game engine to animate meshes via a vertex shader.

### Mesh Morpher

Used to store vertex offsets between a meshes shape keys in it's UV layers. Optionally vertex normals from it's second shape key can be stored in it's vertex colors.

### Vertex Animation

Used to store vertex offsets and normals of selected mesh objects per frame into image textures.

## Example

1. Open Blender and go to **Edit > Preferences > Add-ons > Install**, then
   select `mesh_morpher.py` (or `vertex_animation.py`).
2. Enable the add-on by ticking the checkbox next to its name.
3. In the 3D Viewport, open the sidebar (**N** key) and navigate to the
   **Unreal Tools** tab to find the tool's panel.
4. For **Mesh Morpher**: select a mesh with shape keys and click the operator
   button to bake the vertex offsets into UV layers.
5. For **Vertex Animation**: select mesh objects, set the frame range, and run
   the operator to export per-frame vertex data into image textures ready for
   use in a game engine vertex shader.

## Getting Started

These tools can be installed as add-ons or ran as scripts. Each tool has a panel located in the 3D View's sidebar under the Unreal Tools tab.

### Installing as an Add-on

* First download and unzip files into desired directory.

* While in Blender open the user preferences window.

**Edit > Preferences**

* Navigate the the **add-ons** tab.

* Click the option to **install**.

* A file browser will open.

* Navigate to directory containing the tools.

* Select the tool you want install.

* Then click **install add-on**.

### Running as a Script

* First download and unzip files into desired directory.

* While in Blender use the text editor to open the tool you want to use.

* Then either click the run script operator (the **arrow** icon in header) or use **alt+p** shortcut.
