#!/usr/bin/python3
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import os.path

from vismach import *
import hal

# --------------------------------------------------------------------------
# Visualization model of the 6axis Mecademic Meca500 Robot
# --------------------------------------------------------------------------


from typing import Any, List

MODEL_DIR = "/usr/local/share/meca500/share/models/"

NUM_JOINTS = 6
NUM_LINKS = 7

COL_MACH = [0.9, 0.9, 0.9, 1]  # Greyish?
COL_RED = [1, 0, 0, 1]
COL_BLUE = [0, 0, 1, 1]
COL_GREEN = [0, 1, 0, 1]
COL_X_AXIS = COL_RED
COL_Y_AXIS = COL_BLUE
COL_Z_AXIS = COL_GREEN

SIZE_AXIS = CoordsBase(0, 3, 100, 3)
SIZE_AXIS0 = CoordsBase(0, 5, 200, 5)
SIZE_LINK = CoordsBase(1, 3, 100, 3)

X_TRANS = [0,    0,   0, -38,  0,  0, 0,   0]
Z_TRANS = [91, 135, 135,  61, 61, 61, 0, 100]

TH_ROT = [0, 1, 1, 1, 1, 1, 1, 0]
X_ROT = [0, 0, 0, 0, 0, 0, 0, 0]
Y_ROT = [0, 0, 1, 1, 0, 1, 0, 0]
Z_ROT = [0, 1, 0, 0, 1, 0, 1, 0]


def load_file(file_name):
    """Check for validity paths"""
    if os.path.exists(file_name):
        return AsciiOBJ(file_name)
    else:
        print(f"Warning: {file_name} not found")
        return Color(COL_MACH, [CylinderX(0, 3, 100, 3)])


def print_debug(msg):
    print(f"MECAGUI: {msg}")


c = hal.component("meca500gui")
for i in range(NUM_JOINTS):
    c.newpin(f"joint{i + 1}", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("tool_length", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("plotclear", hal.HAL_BIT, hal.HAL_IN)
c.ready()

work = Capture()
tooltip = Capture()
tool = Capture()
tool = Collection([tooltip, tool])

# create visual tool coordinates axes	
xaxis = Color(COL_X_AXIS, [CylinderX(0, 5, 100, 5)])
yaxis = Color(COL_Y_AXIS, [CylinderY(0, 5, 100, 5)])
zaxis = Color(COL_Z_AXIS, [CylinderZ(0, 5, 100, 5)])
finger1 = Collection([tool, xaxis, yaxis, zaxis])
finger1 = Translate([finger1], 12.5, -20.0, -40)

try:  # Expect files in working directory
    links: List[Any] = [None] * 8
    links[7] = AsciiOBJ(filename=f"{MODEL_DIR}/spindle_assembly.obj")
    links[7] = Color(COL_GREEN, [links[7]])

    for i in range(NUM_LINKS):
        links[i] = load_file(f"{MODEL_DIR}/meca500_link{i + 1}.obj")
        links[i] = Color(COL_MACH, [links[i]])
        print_debug(f"Loaded: {MODEL_DIR}/meca500_link{i + 1}.obj ")

    table = AsciiOBJ(filename=f"{MODEL_DIR}/meca500_table.obj")
    print_debug(f"Loaded: {MODEL_DIR}/meca500_table.obj")
except Exception as detail:
    print(detail)
    raise SystemExit("meca500 requires files in models directory")


links[7] = Collection([finger1, links[7]])
links[7] = Rotate([links[7]], -180, 0, 0, 1)

for i in range(NUM_LINKS - 1 , 0, -1):

    links[i] = Collection([links[i+1], links[i]])
    links[i] = Translate([links[i]], X_TRANS[i], 0, Z_TRANS[i])
    if i == 3:
        links[i] = Rotate([links[i]], 90, 0, 1, 0)
    links[i] = HalRotate([links[i]], c, f"joint{i}", TH_ROT[i], X_ROT[i], Y_ROT[i], Z_ROT[i])

links[0] = Translate([links[0]], 0, 0, 91)
meca500 = Collection([links[1], links[0]])

# create visual world coordinates
xaxis0 = Color(COL_X_AXIS, [CylinderX(0, 5, 200, 5)])
yaxis0 = Color(COL_Y_AXIS, [CylinderY(0, 5, 200, 5)])
zaxis0 = Color(COL_Z_AXIS, [CylinderZ(0, 5, 200, 5)])
coordw = Collection([xaxis0, yaxis0, zaxis0])

# create machine table
table = Color(COL_MACH, [table])
table = Collection([table, coordw])
model = Collection([tooltip, meca500, table, work])

main(model, tooltip, work, 600, 600, None, -75, 300)
