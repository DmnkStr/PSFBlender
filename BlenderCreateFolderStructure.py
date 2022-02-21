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

  index = 1

  structure_type: EnumProperty(
    name="Structure Type",
      items=(('Assets', "Asset", ""),
            ('Project', "Project", ""),
            ),
        default='Asset',
      )

  def execute(self, context):
    self.asset_structure = {
      f'{self.filepath}': {
        '01 Reference': {},
        '02 Geometry': {
          'BaseMesh': {},
          'HighPoly': {
            f'{self.filepath}_high.fbx': {},
          }
        },
        '03 Texture': {
          f'{self.filepath}Color.png': {},
          f'{self.filepath}Roughness.png': {},
          f'{self.filepath}Normal.png': {},
        },
        '04 Animation': {
          f'{self.filepath}AnimationName.fbx': {},
        },
        '05 Simulation': {
          'Cache': {},
        },
        '06 Audio': {},
        '07 Render': {},
        '08 Documentation': {},
        '09 Autosaves': {},
        '10 Trash': {},
        f'{self.filepath}.blend': {},
        f'{self.filepath}.ZPR': {},
        f'{self.filepath}.spp': {},
      }
    }

    self.create_structure(self.asset_structure, '')

    return {'FINISHED'}

  def create_structure(self, struct, path):
    for folder in struct:
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