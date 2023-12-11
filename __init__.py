# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# This addon was created with the Serpens - Visual Scripting Addon.
# This code is generated from nodes and is not intended for manual editing.
# You can find out more about Serpens at <https://blendermarket.com/products/serpens>.


bl_info = {
    "name": "Enabled Linked",
    "description": "Enabled Link by double clicking on the topology in edit mode",
    "author": "Steven Scott",
    "version": (1, 2, 0),
    "blender": (3, 0, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


###############   IMPORTS
import bpy
from bpy.utils import previews
import os
import math


###############   INITALIZE VARIABLES
###############   SERPENS FUNCTIONS
def exec_line(line):
    exec(line)

def sn_print(tree_name, *args):
    if tree_name in bpy.data.node_groups:
        item = bpy.data.node_groups[tree_name].sn_graphs[0].prints.add()
        for arg in args:
            item.value += str(arg) + ";;;"
        if bpy.context and bpy.context.screen:
            for area in bpy.context.screen.areas:
                area.tag_redraw()
    print(*args)

def sn_cast_string(value):
    return str(value)

def sn_cast_boolean(value):
    if type(value) == tuple:
        for data in value:
            if bool(data):
                return True
        return False
    return bool(value)

def sn_cast_float(value):
    if type(value) == str:
        try:
            value = float(value)
            return value
        except:
            return float(bool(value))
    elif type(value) == tuple:
        return float(value[0])
    elif type(value) == list:
        return float(len(value))
    elif not type(value) in [float, int, bool]:
        try:
            value = len(value)
            return float(value)
        except:
            return float(bool(value))
    return float(value)

def sn_cast_int(value):
    return int(sn_cast_float(value))

def sn_cast_boolean_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(bool(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(bool(value[i]) if len(value) > i else bool(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_boolean_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_boolean_vector(value, size)
        except:
            return sn_cast_boolean_vector(bool(value), size)

def sn_cast_float_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value[i]) if len(value) > i else sn_cast_float(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_float_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_float_vector(value, size)
        except:
            return sn_cast_float_vector(sn_cast_float(value), size)

def sn_cast_int_vector(value, size):
    return tuple(map(int, sn_cast_float_vector(value, size)))

def sn_cast_color(value, use_alpha):
    length = 4 if use_alpha else 3
    value = sn_cast_float_vector(value, length)
    tuple_list = []
    for data in range(length):
        data = value[data] if len(value) > data else value[0]
        tuple_list.append(sn_cast_float(min(1, max(0, data))))
    return tuple(tuple_list)

def sn_cast_list(value):
    if type(value) in [str, tuple, list]:
        return list(value)
    elif type(value) in [int, float, bool]:
        return [value]
    else:
        try:
            value = list(value)
            return value
        except:
            return [value]

def sn_cast_blend_data(value):
    if hasattr(value, "bl_rna"):
        return value
    elif type(value) in [tuple, bool, int, float, list]:
        return None
    elif type(value) == str:
        try:
            value = eval(value)
            return value
        except:
            return None
    else:
        return None

def sn_cast_enum(string, enum_values):
    for item in enum_values:
        if item[1] == string:
            return item[0]
        elif item[0] == string.upper():
            return item[0]
    return string


###############   IMPERATIVE CODE
#######   Enabled Linked
addon_keymaps = {}


###############   EVALUATED CODE
#######   Enabled Linked
def sn_prepend_menu_7F779(self,context):
    try:
        layout = self.layout
        if "EDIT_MESH"==bpy.context.mode:
            layout.prop(bpy.context.scene,'enabled_link_mode',icon_value=613,text=r"",emboss=True,toggle=False,invert_checkbox=False,)
        else:
            pass
    except Exception as exc:
        print(str(exc) + " | Error in View3D Mt Editor Menus when adding to menu")


class SNA_OT_Enabled_Link(bpy.types.Operator):
    bl_idname = "sna.enabled_link"
    bl_label = "Enabled Link"
    bl_description = "Enabled Linked Mode on Double Click"
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return "EDIT_MESH"==bpy.context.mode and bpy.context.scene.enabled_link_mode # check we're in edit mode before executing

    def execute(self, context):
        try:
            bpy.ops.mesh.select_linked('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',delimit={sn_cast_enum(r"NORMAL", [("NORMAL","Normal","Delimit by face directions"),("MATERIAL","Material","Delimit by face material"),("SEAM","Seam","Delimit by edge seams"),("SHARP","Sharp","Delimit by sharp edges"),("UV","UVs","Delimit by UV coordinates"),])},)
            bpy.ops.view3d.snap_cursor_to_selected() # custom addition
        except Exception as exc:
            print(str(exc) + " | Error in execute function of Enabled Link")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of Enabled Link")
        return self.execute(context)

def register_key_7379D():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("sna.enabled_link",
                                    type= "LEFTMOUSE",
                                    value= "DOUBLE_CLICK",
                                    repeat= False,
                                    ctrl=False,
                                    alt=False,
                                    shift=False)
        addon_keymaps['7379D'] = (km, kmi)

def register_key_7379E():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("sna.enabled_link",
                                    type= "LEFTMOUSE",
                                    value= "DOUBLE_CLICK",
                                    repeat= False,
                                    ctrl=False,
                                    alt=False,
                                    shift=True)
        addon_keymaps['7379E'] = (km, kmi)


###############   REGISTER ICONS
def sn_register_icons():
    icons = []
    bpy.types.Scene.enabled_linked_icons = bpy.utils.previews.new()
    icons_dir = os.path.join( os.path.dirname( __file__ ), "icons" )
    for icon in icons:
        bpy.types.Scene.enabled_linked_icons.load( icon, os.path.join( icons_dir, icon + ".png" ), 'IMAGE' )

def sn_unregister_icons():
    bpy.utils.previews.remove( bpy.types.Scene.enabled_linked_icons )


###############   REGISTER PROPERTIES
def sn_register_properties():
    bpy.types.Scene.enabled_link_mode = bpy.props.BoolProperty(name='Enabled Link Mode',description='',options=set(),default=True)

def sn_unregister_properties():
    del bpy.types.Scene.enabled_link_mode


###############   REGISTER ADDON
def register():
    sn_register_icons()
    sn_register_properties()
    bpy.utils.register_class(SNA_OT_Enabled_Link)
    register_key_7379D()
    register_key_7379E()
    bpy.types.VIEW3D_MT_editor_menus.prepend(sn_prepend_menu_7F779)


###############   UNREGISTER ADDON
def unregister():
    sn_unregister_icons()
    sn_unregister_properties()
    bpy.types.VIEW3D_MT_editor_menus.remove(sn_prepend_menu_7F779)
    for key in addon_keymaps:
        km, kmi = addon_keymaps[key]
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_OT_Enabled_Link)