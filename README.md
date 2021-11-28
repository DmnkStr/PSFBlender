# BlenderCreateFolderStructure
Simple Add-on to create a folder structure in Blender.

### Installation
1. Download BlenderCreateFolderStructure.py
2. Open Blender
3. Go to Edit > Preferences > Add-ons > Install...
4. Choose BlenderCreateFolderStructure.py

### Instruction
1. Choose File > Create Folder Structure
2. Choose a structure type
3. Choose a location and a name
4. Press Create Folder Structure

Code:
```
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


import os
import bpy
import bpy_extras
from bpy.props import EnumProperty


class CreateFolderStructure(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    """Create Folder Structure"""
    bl_idname = "wm.create_folder_structure"
    bl_label = "Create Folder Structure"
 
    filename_ext = ""

    index = 0

    structure_type: EnumProperty(
            name="Structure Type",
            items=(('Prop', "Prop", ""),
                   ('Character', "Character", ""),
                   ('Environment', "Environment", ""),
                   ('Project', "Project", ""),
                   ),
            default='Prop',
            )

    def execute(self, context):

        self.base_structure()

        if self.structure_type == 'Prop':
            self.reference_structure()
            self.geometry_structure()
            self.texture_structure()
            self.rig_structure()
            self.animation_structure()
            self.audio_structure()

        if self.structure_type == 'Character':
            self.reference_structure()
            self.geometry_structure()
            self.texture_structure()
            self.rig_structure()
            self.animation_structure()
            self.audio_structure()

        if self.structure_type == 'Environment':
            self.simulation_structure()
            self.audio_structure()

        if self.structure_type == 'Project':
            self.props_structure()
            self.characters_structure()
            self.environment_structure()

        self.rendering_structure()
        self.documentation_structure()
        self.autosave_structure()
        self.trash_structure()
        
        return {'FINISHED'}

    def base_structure(self):
        os.mkdir(self.filepath)
        open(os.path.join(self.filepath, os.path.basename(self.filepath)+'.blend'), 'a').close()
        open(os.path.join(self.filepath, os.path.basename(self.filepath)+'.fbx'), 'a').close()

    def reference_structure(self):
        os.mkdir(os.path.join(self.filepath, str(self.index).zfill(2)+' References'))
        self.index += 1

    def props_structure(self):
        os.mkdir(os.path.join(self.filepath, str(self.index).zfill(2)+' Props'))
        open(os.path.join(self.filepath, ' - Create prop folder structures in here - '), 'a').close()
        self.index += 1

    def characters_structure(self):
        os.mkdir(os.path.join(self.filepath, str(self.index).zfill(2)+' Characters'))
        open(os.path.join(self.filepath, ' - Create character folder structures in here - '), 'a').close()
        self.index += 1

    def environment_structure(self):
        os.mkdir(os.path.join(self.filepath, str(self.index).zfill(2)+' Environment'))
        open(os.path.join(self.filepath, ' - Create environment folder structures in here - '), 'a').close()
        self.index += 1

    def geometry_structure(self):
        geometry_path = os.path.join(self.filepath, str(self.index).zfill(2)+' Geometry')
        os.mkdir(geometry_path)
        open(os.path.join(geometry_path, ' - Contains a blender and zbrush file for low and high poly models - '), 'a').close()
        open(os.path.join(geometry_path, 'Geometry.blend'), 'a').close()
        open(os.path.join(geometry_path, 'Geometry.zpr'), 'a').close()
        os.mkdir(os.path.join(geometry_path, 'BaseMeshes'))
        open(os.path.join(geometry_path, 'BaseMeshes', '- Contains all base meshes, you need to model or sculpt -'), 'a').close()
        open(os.path.join(geometry_path, 'BaseMeshes', 'MeshNameBase.fbx'), 'a').close()
        os.mkdir(os.path.join(geometry_path, 'HighPoly'))
        open(os.path.join(geometry_path, 'HighPoly', '- Contains the high poly fbx files for texture baking -'), 'a').close()
        open(os.path.join(geometry_path, 'HighPoly', 'MeshName_high.fbx'), 'a').close()
        self.index += 1

    def texture_structure(self):
        texture_path = os.path.join(self.filepath, str(self.index).zfill(2)+' Texture')
        os.mkdir(texture_path)
        open(os.path.join(texture_path, ' - Contains a substance painter file and folders with exported texture sets - '), 'a').close()
        open(os.path.join(texture_path, 'Texture.blend'), 'a').close()
        open(os.path.join(texture_path, os.path.basename(self.filepath)+'.spp'), 'a').close()
        self.index += 1

    def rig_structure(self):
        rig_path = os.path.join(self.filepath, str(self.index).zfill(2)+' Rig')
        os.mkdir(rig_path)
        open(os.path.join(rig_path, ' - Contains the rigged model - '), 'a').close()
        open(os.path.join(rig_path, 'Rig.blend'), 'a').close()
        self.index += 1

    def animation_structure(self):
        animation_path = os.path.join(self.filepath, str(self.index).zfill(2)+' Animation')
        os.mkdir(animation_path)
        open(os.path.join(animation_path, ' - Contains one blender file with all animations and all animations exported as fbx files - '), 'a').close()
        open(os.path.join(animation_path, 'Animation.blend'), 'a').close()
        open(os.path.join(animation_path, 'AnimationName.fbx'), 'a').close()
        self.index += 1

    def simulation_structure(self):
        simulation_path = os.path.join(self.filepath, str(self.index).zfill(2)+' Simulation')
        os.mkdir(simulation_path)
        open(os.path.join(simulation_path, ' - Contains blender files with the simulations and a cache folder with cached simulations - '), 'a').close()
        open(os.path.join(simulation_path, 'SimulationName.blend'), 'a').close()
        os.mkdir(os.path.join(simulation_path, 'Cache'))
        open(os.path.join(simulation_path,'Cache' , ' - Contains folders with cached simulations - '), 'a').close()
        self.index += 1

    def rendering_structure(self):
        render_path = os.path.join(self.filepath, str(self.index).zfill(2)+' Render')
        os.mkdir(render_path)
        open(os.path.join(render_path, 'RenderName.blend'), 'a').close()
        open(os.path.join(render_path, ' - Contains blender files to render and folders with rendered images - '), 'a').close()
        self.index += 1

    def audio_structure(self):
        path = os.path.join(self.filepath, str(self.index).zfill(2)+' Audio')
        os.mkdir(path)
        open(os.path.join(path, ' - Contains audio files - '), 'a').close()
        self.index += 1

    def documentation_structure(self):
        path = os.path.join(self.filepath, str(self.index).zfill(2)+' Documentation')
        os.mkdir(path)
        open(os.path.join(path, ' - Contains screenshots, gifs and other forms of documentation - '), 'a').close()
        self.index += 1

    def research_structure(self):
        research_path = os.path.join(self.filepath, 'Research')
        os.mkdir(os.path.join(self.filepath, 'Research'))
        os.mkdir(os.path.join(self.filepath, 'Research', 'Experiments'))
        os.mkdir(os.path.join(self.filepath, 'Research', 'Scripts'))
        self.index += 1

    def autosave_structure(self):
        path = os.path.join(self.filepath, str(self.index).zfill(2)+' Autosave')
        os.mkdir(path)
        open(os.path.join(path, ' - Contains autosaves - '), 'a').close()
        self.index += 1

    def trash_structure(self):
        path = os.path.join(self.filepath, str(self.index).zfill(2)+' Autosave')
        os.mkdir(path)
        open(os.path.join(path, ' - Contains temporary files which can be deleted - '), 'a').close()
        self.index += 1


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
```
