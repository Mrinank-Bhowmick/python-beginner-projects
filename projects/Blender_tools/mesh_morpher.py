bl_info = {
    "name": "Mesh Morpher",
    "author": "ibra-kdbra",
    "version": (1, 0),
    "blender": (4, 0, 1),
    "location": "View3D > Sidebar > Unreal Tools Tab",
    "description": "A tool for storing shape key data for use in a vertex shader.",
    "warning": "",
    "doc_url": "",
    "category": "Unreal Tools",
}


import bpy


def pack_normals(me):
    """Stores normals in a given mesh's vertex colors"""
    if not me.vertex_colors:
        me.vertex_colors.new()
    col = me.vertex_colors[0]
    col.name = "normals"
    key = me.shape_keys.key_blocks[1]
    normals = list(zip(*[iter(key.normals_vertex_get())] * 3))
    for loop in me.loops:
        r, g, b = normals[loop.vertex_index]
        col.data[loop.index].color = ((r + 1) * 0.5, (-g + 1) * 0.5, (b + 1) * 0.5, 1)


def get_shape_key_offsets(shape_keys, two_shape_keys=False):
    """Return a list of vertex offsets between shape keys"""
    keys = shape_keys.key_blocks
    offsets = []
    original = keys[0].data
    target = keys[1].data
    offset = [v1.co - v2.co for v1, v2 in zip(target, original)]
    offsets.append(offset)
    if two_shape_keys:
        target = keys[2].data
        offset = [v1.co - v2.co for v1, v2 in zip(target, original)]
        offsets.append(offset)
    return offsets


def pack_offsets(ob, offsets):
    """Stores shape key vertex offsets in mesh's UVs"""
    me = ob.data
    while len(me.uv_layers) < 4:
        me.uv_layers.new()
    for loop in me.loops:
        x1, y1, z1 = offsets[0][loop.vertex_index]
        if len(offsets) > 1:
            offset = offsets[1][loop.vertex_index]
        else:
            offset = ob.location
        x2, y2, z2 = offset
        me.uv_layers[1].data[loop.index].uv = (x2, 1 - (-y2))
        me.uv_layers[2].data[loop.index].uv = (z2, 1 - x1)
        me.uv_layers[3].data[loop.index].uv = (-y1, 1 - z1)


class MeshMorpherSettings(bpy.types.PropertyGroup):
    store_shape_key1_normals: bpy.props.BoolProperty(
        name="First Shape Key Normals",
        description="Store first shape key's vertex normals in vertex colors",
        default=True,
    )
    two_shape_keys: bpy.props.BoolProperty(
        name="Two Shape Keys",
        description="Store vertex offsets for first and second shape keys",
        default=False,
    )


class OBJECT_OT_ProcessShapeKeys(bpy.types.Operator):
    """Store object's shape key offsets in it's UV layers"""

    bl_idname = "object.process_shape_keys"
    bl_label = "Process Shape Keys"

    store_shape_key1_normals: bpy.props.BoolProperty(
        name="First Shape Key Normals", default=True
    )
    two_shape_keys: bpy.props.BoolProperty(name="Two Shape Keys", default=False)

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob and ob.type == "MESH" and ob.mode == "OBJECT"

    def execute(self, context):
        units = context.scene.unit_settings
        ob = context.object
        shape_keys = ob.data.shape_keys
        if units.system != "METRIC" or round(units.scale_length, 2) != 0.01:
            self.report(
                {"ERROR"}, "Scene Units must be Metric with a Unit Scale of 0.01!"
            )
            return {"CANCELLED"}
        if not shape_keys:
            self.report({"ERROR"}, "Object has no shape keys!")
            return {"CANCELLED"}
        if len(shape_keys.key_blocks) < 2 + self.two_shape_keys:
            self.report({"ERROR"}, "Object needs additional shape keys!")
            return {"CANCELLED"}
        if self.store_shape_key1_normals:
            pack_normals(ob.data)
        offsets = get_shape_key_offsets(shape_keys, self.two_shape_keys)
        pack_offsets(ob, offsets)
        return {"FINISHED"}


class VIEW3D_PT_MeshMorpher(bpy.types.Panel):
    """Creates a Panel in 3D Viewport"""

    bl_label = "Mesh Morpher"
    bl_idname = "VIEW3D_PT_mesh_morpher"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Unreal Tools"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        props = context.scene.mesh_morpher_settings
        col.prop(props, "store_shape_key1_normals")
        col.prop(props, "two_shape_keys")
        op = col.operator("object.process_shape_keys")
        op.store_shape_key1_normals = props.store_shape_key1_normals
        op.two_shape_keys = props.two_shape_keys


def register():
    bpy.utils.register_class(MeshMorpherSettings)
    bpy.utils.register_class(OBJECT_OT_ProcessShapeKeys)
    bpy.utils.register_class(VIEW3D_PT_MeshMorpher)
    bpy.types.Scene.mesh_morpher_settings = bpy.props.PointerProperty(
        type=MeshMorpherSettings
    )


def unregister():
    bpy.utils.unregister_class(MeshMorpherSettings)
    bpy.utils.unregister_class(OBJECT_OT_ProcessShapeKeys)
    bpy.utils.unregister_class(VIEW3D_PT_MeshMorpher)
    del bpy.types.Scene.mesh_morpher_settings


if __name__ == "__main__":
    register()
