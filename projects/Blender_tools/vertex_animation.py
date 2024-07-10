bl_info = {
    "name": "Vertex Animation",
    "author": "ibra-kdbra",
    "version": (1, 0),
    "blender": (4, 0, 1),
    "location": "View3D > Sidebar > Unreal Tools Tab",
    "description": "A tool for storing per frame vertex data for use in a vertex shader.",
    "warning": "",
    "doc_url": "",
    "category": "Unreal Tools",
}


import bpy
import bmesh


def get_per_frame_mesh_data(context, data, objects):
    """Return a list of combined mesh data per frame"""
    meshes = []
    for i in frame_range(context.scene):
        context.scene.frame_set(i)
        depsgraph = context.evaluated_depsgraph_get()
        bm = bmesh.new()
        for ob in objects:
            eval_object = ob.evaluated_get(depsgraph)
            me = data.meshes.new_from_object(eval_object)
            me.transform(ob.matrix_world)
            bm.from_mesh(me)
            data.meshes.remove(me)
        me = data.meshes.new("mesh")
        bm.normal_update()
        bm.to_mesh(me)
        bm.free()
        me.update()
        meshes.append(me)
    return meshes


def create_export_mesh_object(context, data, me):
    """Return a mesh object with correct UVs"""
    while len(me.uv_layers) < 2:
        me.uv_layers.new()
    uv_layer = me.uv_layers[1]
    uv_layer.name = "vertex_anim"
    for loop in me.loops:
        uv_layer.data[loop.index].uv = (
            (loop.vertex_index + 0.5) / len(me.vertices),
            128 / 255,
        )
    ob = data.objects.new("export_mesh", me)
    context.scene.collection.objects.link(ob)
    return ob


def get_vertex_data(data, meshes):
    """Return lists of vertex offsets and normals from a list of mesh data"""
    original = meshes[0].vertices
    offsets = []
    normals = []
    for me in reversed(meshes):
        for v in me.vertices:
            offset = v.co - original[v.index].co
            x, y, z = offset
            offsets.extend((x, -y, z, 1))
            x, y, z = v.normal
            normals.extend(((x + 1) * 0.5, (-y + 1) * 0.5, (z + 1) * 0.5, 1))
        if not me.users:
            data.meshes.remove(me)
    return offsets, normals


def frame_range(scene):
    """Return a range object with with scene's frame start, end, and step"""
    return range(scene.frame_start, scene.frame_end, scene.frame_step)


def bake_vertex_data(data, offsets, normals, size):
    """Stores vertex offsets and normals in seperate image textures"""
    width, height = size
    offset_texture = data.images.new(
        name="offsets", width=width, height=height, alpha=True, float_buffer=True
    )
    normal_texture = data.images.new(
        name="normals", width=width, height=height, alpha=True
    )
    offset_texture.pixels = offsets
    normal_texture.pixels = normals


class OBJECT_OT_ProcessAnimMeshes(bpy.types.Operator):
    """Store combined per frame vertex offsets and normals for all
    selected mesh objects into seperate image textures"""

    bl_idname = "object.process_anim_meshes"
    bl_label = "Process Anim Meshes"

    @property
    def allowed_modifiers(self):
        return [
            "ARMATURE",
            "CAST",
            "CURVE",
            "DISPLACE",
            "HOOK",
            "LAPLACIANDEFORM",
            "LATTICE",
            "MESH_DEFORM",
            "SHRINKWRAP",
            "SIMPLE_DEFORM",
            "SMOOTH",
            "CORRECTIVE_SMOOTH",
            "LAPLACIANSMOOTH",
            "SURFACE_DEFORM",
            "WARP",
            "WAVE",
        ]

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob and ob.type == "MESH" and ob.mode == "OBJECT"

    def execute(self, context):
        units = context.scene.unit_settings
        data = bpy.data
        objects = [ob for ob in context.selected_objects if ob.type == "MESH"]
        vertex_count = sum([len(ob.data.vertices) for ob in objects])
        frame_count = len(frame_range(context.scene))
        for ob in objects:
            for mod in ob.modifiers:
                if mod.type not in self.allowed_modifiers:
                    self.report(
                        {"ERROR"},
                        f"Objects with {mod.type.title()} modifiers are not allowed!",
                    )
                    return {"CANCELLED"}
        if units.system != "METRIC" or round(units.scale_length, 2) != 0.01:
            self.report(
                {"ERROR"}, "Scene Unit must be Metric with a Unit Scale of 0.01!"
            )
            return {"CANCELLED"}
        if vertex_count > 8192:
            self.report(
                {"ERROR"},
                f"Vertex count of {vertex_count :,}, execedes limit of 8,192!",
            )
            return {"CANCELLED"}
        if frame_count > 8192:
            self.report(
                {"ERROR"}, f"Frame count of {frame_count :,}, execedes limit of 8,192!"
            )
            return {"CANCELLED"}
        meshes = get_per_frame_mesh_data(context, data, objects)
        export_mesh_data = meshes[0].copy()
        create_export_mesh_object(context, data, export_mesh_data)
        offsets, normals = get_vertex_data(data, meshes)
        texture_size = vertex_count, frame_count
        bake_vertex_data(data, offsets, normals, texture_size)
        return {"FINISHED"}


class VIEW3D_PT_VertexAnimation(bpy.types.Panel):
    """Creates a Panel in 3D Viewport"""

    bl_label = "Vertex Animation"
    bl_idname = "VIEW3D_PT_vertex_animation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Unreal Tools"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False
        scene = context.scene
        col = layout.column(align=True)
        col.prop(scene, "frame_start", text="Frame Start")
        col.prop(scene, "frame_end", text="End")
        col.prop(scene, "frame_step", text="Step")
        row = layout.row()
        row.operator("object.process_anim_meshes")


def register():
    bpy.utils.register_class(OBJECT_OT_ProcessAnimMeshes)
    bpy.utils.register_class(VIEW3D_PT_VertexAnimation)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_ProcessAnimMeshes)
    bpy.utils.unregister_class(VIEW3D_PT_VertexAnimation)


if __name__ == "__main__":
    register()
