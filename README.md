# PSFBlender
Project Folder Structure For Blender

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
    "name": "Creates Folder Structure",
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

  index = 1

  structure_type: EnumProperty(
    name="Structure Type",
      items=(('Assets', "Asset", ""),
            ('Project', "Project", ""),
            ),
        default='Assets',
      )

  def execute(self, context):
    self.structure_name = os.path.basename(self.filepath)
    self.asset_structure = {
      f'{self.filepath}': {
        '01 Reference': {},
        '02 Geometry': {
          'BaseMesh': {},
          'HighPoly': {
            f'{self.structure_name}_high.fbx': {},
          }
        },
        '03 Texture': {
          f'{self.structure_name}Color.png': {},
          f'{self.structure_name}Roughness.png': {},
          f'{self.structure_name}Normal.png': {},
        },
        '04 Animation': {
          f'{self.structure_name}AnimationName.fbx': {},
        },
        '05 Simulation': {
          'Cache': {},
        },
        '06 Audio': {},
        '07 Render': {},
        '08 Documentation': {},
        '09 Autosaves': {},
        '10 Trash': {},
        f'{self.structure_name}.blend': {},
        f'{self.structure_name}.ZPR': {},
        f'{self.structure_name}.spp': {},
      }
    }

    self.create_structure(self.asset_structure, '')

    return {'FINISHED'}

  def create_structure(self, struct, path):
    for folder in struct:
      print(os.path.join(path, folder))
      if '.' in folder:
        open( os.path.join(path, folder), 'a' ).close()
      else:
        os.mkdir(os.path.join(path, folder))
      try:
        self.create_structure(struct.get(folder), os.path.join(path, folder))
      except:
        return
    


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
