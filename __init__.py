bl_info = {
    "name": "Create Folder Structure",
    "description": "A simple tool to genereate a folder structure",
    "author": "Dominik Strasser ",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "File > Create Folder Structure",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

### IMPORTS
import os
import bpy
import bpy_extras
from bpy.props import EnumProperty


class CreateFolderStructure(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    """Create Folder Structure"""
    bl_idname = "wm.create_folder_structure"
    bl_label = "Create Folder Structure"
 
    filename_ext = ""

    structure_type: EnumProperty(
            name="Structure Type",
            items=(('Prop', "Prop", ""),
                   ('Character', "Character", ""),
                   ('Scene', "Scene", ""),
                   ('Project', "Project", ""),
                   ),
            default='Prop',
            )

    def execute(self, context):

        os.mkdir(self.filepath)

        ### BASE
        os.mkdir(os.path.join(self.filepath, 'Audio'))
        os.mkdir(os.path.join(self.filepath, 'Autosaves'))
        os.mkdir(os.path.join(self.filepath, 'References'))
        os.mkdir(os.path.join(self.filepath, 'Renderings'))
        os.mkdir(os.path.join(self.filepath, 'Screenshots'))
        os.mkdir(os.path.join(self.filepath, 'Trash'))

        if self.structure_type == 'Prop':
            os.mkdir(os.path.join(self.filepath, 'Animations'))
            open(os.path.join(self.filepath, 'Animations', os.path.basename(self.filepath)+'AnimationName'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Geometry'))
            os.mkdir(os.path.join(self.filepath, 'Geometry', 'BaseMeshes'))
            open(os.path.join(self.filepath, 'Geometry', 'BaseMeshes', 'MeshNameBaseMesh'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Geometry', 'Blendshapes'))
            open(os.path.join(self.filepath, 'Geometry', 'Blendshapes', 'MeshNameBlendshapeName'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Geometry', 'HighPoly'))
            open(os.path.join(self.filepath, 'Geometry', 'HighPoly', 'MeshName_high'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Geometry', 'TexturingBase'))
            open(os.path.join(self.filepath, 'Geometry', 'TexturingBase', os.path.basename(self.filepath)+'TexturingBase'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Rig'))
            open(os.path.join(self.filepath, 'Rig', os.path.basename(self.filepath)+'Rig'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Texture'))
            open(os.path.join(self.filepath, 'Texture', os.path.basename(self.filepath)+'DiffuseNormalAORoughnessMetallic'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Maps'))
            os.mkdir(os.path.join(self.filepath, 'Masks'))

        if self.structure_type == 'Character':
            open(os.path.join(self.filepath, 'Character'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Animations'))
            os.mkdir(os.path.join(self.filepath, 'Geometry'))
            os.mkdir(os.path.join(self.filepath, 'Geometry', 'BaseMeshes'))
            os.mkdir(os.path.join(self.filepath, 'Geometry', 'Blendshapes'))
            os.mkdir(os.path.join(self.filepath, 'Geometry', 'HighPoly'))
            os.mkdir(os.path.join(self.filepath, 'Geometry', 'TexturingBase'))
            os.mkdir(os.path.join(self.filepath, 'Rig'))
            os.mkdir(os.path.join(self.filepath, 'Texture'))
            os.mkdir(os.path.join(self.filepath, 'Maps'))
            os.mkdir(os.path.join(self.filepath, 'Masks'))

        if self.structure_type == 'Scene':
            open(os.path.join(self.filepath, 'Scene'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Maps'))
            os.mkdir(os.path.join(self.filepath, 'Masks'))
            os.mkdir(os.path.join(self.filepath, 'Simulations'))

        if self.structure_type == 'Project':
            open(os.path.join(self.filepath, 'Project'), 'a').close()
            os.mkdir(os.path.join(self.filepath, 'Research'))
            os.mkdir(os.path.join(self.filepath, 'Research', 'Experiments'))
            os.mkdir(os.path.join(self.filepath, 'Research', 'Scripts'))
            os.mkdir(os.path.join(self.filepath, 'MakingOf'))
            os.mkdir(os.path.join(self.filepath, 'Props'))
            os.mkdir(os.path.join(self.filepath, 'Characters'))
            os.mkdir(os.path.join(self.filepath, 'Scenes'))
        
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.separator()
    self.layout.operator(CreateFolderStructure.bl_idname)

def register():
    bpy.types.TOPBAR_MT_file.append(menu_func)
    bpy.utils.register_class(CreateFolderStructure)

def unregister():
    bpy.utils.unregister_class(CreateFolderStructure)
    bpy.types.TOPBAR_MT_file.remove(menu_func)

if __name__ == "__main__":
    register()