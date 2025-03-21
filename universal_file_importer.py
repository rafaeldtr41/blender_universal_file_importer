bl_info = {
    "name": "Universal Clean Importer",
    "author": "Rafael D. Tamayo Rojas",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "File Browser > Import Panel",
    "description": "Safe import of FBX/OBJ/GLTF/BLEND files and opens in another windows for preview",
    "warning": "",
    "doc_url": "",
    "category": "Import-Export",
}

import bpy
from mathutils import Vector
import os


def create_isolated_window():
    """Create a new window with fresh 3D View context"""
    original_screen = bpy.context.window.screen
    bpy.ops.wm.window_new()
    new_window = bpy.context.window
    new_screen = new_window.screen
    
    if not any(a.type == 'VIEW_3D' for a in new_screen.areas):
        new_screen.areas[0].type = 'VIEW_3D'
    
    return new_window, original_screen

def cleanup_isolated_window(new_window, original_screen):
    """Close temporary window and restore original context"""
    bpy.context.window_manager.windows.remove(new_window)
    for win in bpy.context.window_manager.windows:
        if win.screen == original_screen:
            bpy.context.window_manager.windows.active = win
            break

class IMPORT_OT_clean_importer(bpy.types.Operator):
    """Import assets with clean context isolation"""
    bl_idname = "import_scene.clean_importer"
    bl_label = "Clean Import"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        params = context.space_data.params
        if not params.filename:
            self.report({'ERROR'}, "No file selected")
            return {'CANCELLED'}
        
        file_path = os.path.join(
            os.fsdecode(bpy.path.abspath(params.directory)),
            os.fsdecode(params.filename)
        )
        
        file_extension = os.path.splitext(file_path)[1].lower()
        new_window, original_screen = create_isolated_window()
        
        try:
            area = next(a for a in new_window.screen.areas if a.type == 'VIEW_3D')
            region = next(r for r in area.regions if r.type == 'WINDOW')
            override = {
                'window': new_window,
                'screen': new_window.screen,
                'area': area,
                'region': region,
                'scene': new_window.scene,
            }

            with context.temp_override(**override):
                # Clear temporary scene
                bpy.ops.object.select_all(action='SELECT')
                bpy.ops.object.delete()

                # Handle different file types
                if file_extension == ".fbx":
                    bpy.ops.import_scene.fbx(filepath=file_path)
                elif file_extension == ".obj":
                    bpy.ops.wm.obj_import(filepath=file_path)
                elif file_extension in {".glb", ".gltf"}:
                    bpy.ops.import_scene.gltf(filepath=file_path)
                elif file_extension == ".blend":
                    with bpy.data.libraries.load(file_path) as (data_from, data_to):
                        data_to.objects = data_from.objects
                    for obj in data_to.objects:
                        if obj and isinstance(obj, bpy.types.Object):
                            try:
                                context.scene.collection.objects.link(obj)
                            except RuntimeError:
                                continue
                else:
                    self.report({'ERROR'}, "Unsupported file format")
                    return {'CANCELLED'}

            # Transfer objects to main scene
            for obj in new_window.scene.objects:
                context.scene.collection.objects.link(obj)
                new_window.scene.collection.objects.unlink(obj)

            return {'FINISHED'}

        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}
        finally:
            cleanup_isolated_window(new_window, original_screen)

class FILEBROWSER_PT_clean_import_panel(bpy.types.Panel):
    """File Browser Import Panel"""
    bl_label = "Clean Import"
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_category = "Import"

    def draw(self, context):
        layout = self.layout
        params = context.space_data.params
        layout.active = bool(params.filename)
        
        layout.operator(IMPORT_OT_clean_importer.bl_idname)
        context.space_data.params.filter_glob = "*.fbx;*.obj;*.glb;*.gltf;*.blend"

def register():
    # Ensure required importers are enabled
    for addon in ['io_scene_obj', 'io_scene_fbx', 'io_scene_gltf2']:
        try:
            bpy.ops.preferences.addon_enable(module=addon)
        except Exception:
            pass
    
    bpy.utils.register_class(IMPORT_OT_clean_importer)
    bpy.utils.register_class(FILEBROWSER_PT_clean_import_panel)

def unregister():
    bpy.utils.unregister_class(FILEBROWSER_PT_clean_import_panel)
    bpy.utils.unregister_class(IMPORT_OT_clean_importer)

if __name__ == "__main__":
    register()