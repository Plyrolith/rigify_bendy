#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

# <pep8 compliant>

import bpy

from rigify.utils.widgets_basic import create_circle_widget

from .spine_rigs import BaseBendyHeadTailRig
from .basic_tentacle import Rig as BasicTentacleRig


class Rig(BasicTentacleRig, BaseBendyHeadTailRig):
    """
    Bendy tail rig with connect option.
    """

    # Widgets
    def make_control_widget(self, i, ctrl):
        create_circle_widget(self.obj, ctrl, radius=0.5, head_tail=0.75)


def create_sample(obj, *, parent=None):
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    bones = {}

    bone = arm.edit_bones.new('tail')
    bone.head[:] = 0.0000, 0.0552, 1.0099
    bone.tail[:] = -0.0000, 0.0582, 0.8669
    bone.roll = 0.0000
    bone.use_connect = False
    if parent:
        bone.parent = arm.edit_bones[parent]
    bones['tail'] = bone.name
    bone = arm.edit_bones.new('tail.001')
    bone.head[:] = -0.0000, 0.0582, 0.8669
    bone.tail[:] = -0.0000, 0.0365, 0.7674
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['tail']]
    bones['tail.001'] = bone.name
    bone = arm.edit_bones.new('tail.002')
    bone.head[:] = -0.0000, 0.0365, 0.7674
    bone.tail[:] = -0.0000, 0.0010, 0.6984
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['tail.001']]
    bones['tail.002'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['tail']]
    pbone.rigify_type = 'spines_bendy.basic_tail'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    try:
        pbone.rigify_parameters.connect_chain = bool(parent)
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.tweak_layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.copy_rotation_axes = [True, True, True]
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['tail.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone = obj.pose.bones[bones['tail.002']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        arm.edit_bones.active = bone
