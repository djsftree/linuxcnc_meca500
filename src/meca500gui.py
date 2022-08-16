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
import math
import sys

# --------------------------------------------------------------------------
# Visualization model of the 6axis Mecademic Meca500 Robot
# --------------------------------------------------------------------------


# give endpoint Z values and radii
# resulting cylinder is on the Z axis
class HalToolCylinder(CylinderZ):
    def __init__(self, comp, *args):
        CylinderZ.__init__(self, *args)
        self.comp = comp

    def coords(self):
        return (0, self.comp["tool-radius"], self.comp["tool-length"], self.comp["tool-radius"])
        

from typing import Any, List

MODEL_DIR = "/usr/local/share/meca500/share/models"

NUM_JOINTS = 6
NUM_LINKS = 7

COL_MACH =  [0.9, 0.9, 0.9,  1]  # Greyish?
COL_RED =   [  1,   0,   0,  1]
COL_BLUE =  [  0,   0,   1,  1]
COL_GREEN = [  0,   1,   0,  1]

COL_X_AXIS = COL_RED
COL_Y_AXIS = COL_GREEN
COL_Z_AXIS = COL_BLUE
COLOURS = [COL_MACH] * NUM_LINKS
COLOURS[5] = [0.2, 0.6, 0.2, 1]



LINK_NAMES = ["BASE",  "A1",   "A2",   "A3",   "A4",    "A5",   "A6",   "SPINDLE"]
X_TRANS =    [0,         0,    135,     38,       0,       0,     0,       0]
Z_TRANS =    [0,       135,      0,  -61.5,   -58.5,     -70,     0,       0]
TH_ROT =     [0,         1,      1,      1,       1,       1,     1,       0]
X_ROT =      [0,         0,      0,      0,       0,       0,     0,       0]
Y_ROT =      [0,         0,      1,      1,       0,       1,     0,       0]
Z_ROT =      [0,         1,      0,      0,      -1,       0,    -1,       0]



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
c.newpin("tool-length", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("tool-radius", hal.HAL_FLOAT, hal.HAL_IN)
c.ready()

pivot_len=100
tool_radius=0.25
tooltip = Capture()
tool = Collection([
        HalTranslate([tooltip], c, "tool-length", 0, 0, 1),
        HalToolCylinder(c),
        ])
tool = Translate([tool], 0, 0, -3)
tool = Color([1,0,0,0], [tool] )


work = Capture()


# create visual tool coordinates axes	
xaxis = Color(COL_X_AXIS, [CylinderX(0, 2, 150, 2)])
yaxis = Color(COL_Y_AXIS, [CylinderY(0, 2, 150, 2)])
zaxis = Color(COL_Z_AXIS, [CylinderZ(0, 2, 150, 2)])
finger1 = Collection([tool, xaxis, yaxis, zaxis])


try:  # Expect files in working directory
    links: List[Any] = [None] * 8
    
    links[0] = AsciiOBJ(filename=f"{MODEL_DIR}/meca500_table.obj")
    print_debug(f"Loaded: {MODEL_DIR}/meca500_table.obj")
    
    for i in range(NUM_LINKS):
        links[i+1] = load_file(f"{MODEL_DIR}/meca500_link{i + 1}.obj")
        links[i+1] = Color(COLOURS[i], [links[i+1]])
        print_debug(f"Loaded: {MODEL_DIR}/meca500_link{i + 1}.obj ")
        
    links[7] = AsciiOBJ(filename=f"{MODEL_DIR}/spindle_assembly.obj")
    links[7] = Color(COL_MACH, [links[7]])
    print_debug(f"Loaded: {MODEL_DIR}/spindle_assembly.obj")

except Exception as detail:
    print(detail)
    raise SystemExit("meca500 requires files in models directory")

# add finger to A6
links[6] = Collection([finger1, links[6]])

for i in range(NUM_LINKS - 1, 0, -1):
    if X_ROT[i+1]:
        links[i] = Collection([links[i + 1], links[i], xaxis])
    elif Y_ROT[i+1]:
        links[i] = Collection([links[i + 1], links[i], yaxis])
    elif Z_ROT[i+1]:
        links[i] = Collection([links[i + 1], links[i], zaxis])
    else:
        links[i] = Collection([links[i + 1], links[i]])
    links[i] = Translate([links[i]], X_TRANS[i], 0, Z_TRANS[i])
    print_debug(f"links[{i}] = Translate([links[{i}]], {X_TRANS[i]}, 0, {Z_TRANS[i]})")
    links[i] = HalRotate([links[i]], c, f"joint{i}", TH_ROT[i], X_ROT[i], Y_ROT[i], Z_ROT[i])
    print_debug(f"links[{i}] = HalRotate([links[{i}]], c, joint{i}, {TH_ROT[i]}, {X_ROT[i]}, {Y_ROT[i]}, {Z_ROT[i]})")
    print("---")


meca500 = Collection([links[1], links[0]])

# create table with a debug finger
xaxis0 = Color(COL_X_AXIS, [CylinderX(0, 2, 200, 2)])
yaxis0 = Color(COL_Y_AXIS, [CylinderY(0, 2, 200, 2)])
zaxis0 = Color(COL_Z_AXIS, [CylinderZ(0, 2, 300, 2)])
coordw = Collection([xaxis0, yaxis0, zaxis0])
table = Color(COL_MACH, [links[0]])
table = Collection([table, coordw])

model = Collection([tooltip, meca500, table, work])
main(model, tooltip, work, size=800, hud=0, lat=0, lon=0)
