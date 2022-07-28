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

from vismach import *
import hal

# --------------------------------------------------------------------------
# Visualization model of the 6axis Mecademic Meca500 Robot
# --------------------------------------------------------------------------


from typing import Any, List

NUM_JOINTS = 6
NUM_LINKS = 7

COL_MACH = [0.9, 0.9, 0.9, 1]  # Greyish?
COL_RED = [1, 0, 0, 1]
COL_BLUE = [0, 1, 0, 1]
COL_GREEN = [0, 0, 1, 1]
COL_X_AXIS = COL_RED
COL_Y_AXIS = COL_BLUE
COL_Z_AXIS = COL_GREEN

SIZE_AXIS = CoordsBase(0, 3, 100, 3)
SIZE_AXIS0 = CoordsBase(0, 5, 200, 5)
SIZE_LINK = CoordsBase(1, 3, 100, 3)

X_TRANS = [0, 0, 0, -38, 0, 0, 0]
Z_TRANS = [91, 135, 135, 61, 61, 61]

TH_ROT = [0, 1, 1, 1, 1, 1, 1]
X_ROT = [0, 0, 0, 0, 1, 0, 1]
Y_ROT = [0, 0, 1, 1, 0, 1, 0]
Z_ROT = [0, 1, 0, 0, 0, 0, 0]

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
xaxis = Color(COL_X_AXIS, [CylinderX(0, 3, 100, 3)])
yaxis = Color(COL_Y_AXIS, [CylinderY(0, 3, 100, 3)])
zaxis = Color(COL_Z_AXIS, [CylinderZ(0, 3, 100, 3)])
finger1 = Collection([tool, xaxis, yaxis, zaxis])

try:  # Expect files in working directory
    link8 = AsciiOBJ(filename="/usr/local/share/meca500/share/models/spindle_assembly.obj")
    link7 = AsciiOBJ(filename="/usr/local/share/meca500/share/models/meca500_link7.obj")
    link6 = AsciiOBJ(filename="/usr/local/share/meca500/share/models/meca500_link6.obj")
    link5 = AsciiOBJ(filename="/usr/local/share/meca500/share/models/meca500_link5.obj")
    link4 = AsciiOBJ(filename="/usr/local/share/meca500/share/models/meca500_link4.obj")
    link3 = AsciiOBJ(filename="/usr/local/share/meca500/share/models/meca500_link3.obj")
    link2 = AsciiOBJ(filename="/usr/local/share/meca500/share/models/meca500_link2.obj")
    link1 = AsciiOBJ(filename="/usr/local/share/meca500/share/models/meca500_link1.obj")
    table = AsciiOBJ(filename="/usr/local/share/meca500/share/models/meca500_table.obj")
except Exception as detail:
    print(detail)
    raise SystemExit("meca500 requires files in models directory")

# create spindle model
link8 = Color(COL_MACH, [link8])
link8 = Translate([link8], 0, 0, 100)
link8 = Rotate([link8], -90, 0, 1, 0)
finger1 = Translate([finger1], 12.5, -20.0, -40)
link8 = Collection([finger1, link8])

### Create link7
link7 = Color(COL_MACH, [link7])
link7 = Collection([link8, link7])
link7 = HalRotate([link7], c, "joint6", 1, 1, 0, 0)

### Create link6
link6 = Color(COL_MACH, [link6])
link6 = Collection([link7, link6])
link6 = Translate([link6], 0, 0, 61)
link6 = HalRotate([link6], c, "joint5", 1, 0, 1, 0)

### Create link5
link5 = Color(COL_MACH, [link5])
link5 = Collection([link6, link5])
link5 = Translate([link5], 0, 0, 61)
link5 = HalRotate([link5], c, "joint4", 1, 1, 0, 0)

### Create link4
link4 = Color(COL_MACH, [link4])
link4 = Collection([link5, link4])
link4 = Translate([link4], -38.0, 0, 61.0)
link4 = Rotate([link4], 90, 0, 1, 0)
link4 = HalRotate([link4], c, "joint3", 1, 0, 1, 0)

### Create link3
link3 = Color(COL_MACH, [link3])
link3 = Collection([link4, link3])
link3 = Translate([link3], 0, 0, 135.0)
link3 = HalRotate([link3], c, "joint2", 1, 0, 1, 0)

### Create link2
link2 = Color(COL_MACH, [link2])
link2 = Collection([link3, link2])
link2 = Translate([link2], 0, 0, 135.0)
link2 = HalRotate([link2], c, "joint1", 1, 0, 0, 1)

### Create link1 stationary base
link1 = Color(COL_MACH, [link1])
link1 = Translate([link1], 0, 0, 91)
meca500 = Collection([link2, link1])

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
