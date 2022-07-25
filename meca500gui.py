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

#--------------------------------------------------------------------------
# Visualization model of the 6axis Mecademic Meca500 Robot
#--------------------------------------------------------------------------

c = hal.component("meca500gui")
c.newpin("joint1", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("joint2", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("joint3", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("joint4", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("joint5", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("joint6", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("tool_length", hal.HAL_FLOAT, hal.HAL_IN)
c.newpin("plotclear", hal.HAL_BIT, hal.HAL_IN)
c.ready()

work = Capture()

# show CNC-tooltip position (ie tool trace in window)
tooltip = Capture()

# create finger (tool)
finger1 = CylinderZ(80, 10, 0, 10)
finger1 = Color([0.9,0.9,0.9,1],[finger1])

# create visual tool coordinates axes
xaxis = Color([1,0,0,1],[CylinderX(0,3,100,3)])
yaxis = Color([0,1,0,1],[CylinderY(0,3,100,3)])
zaxis = Color([0,0,1,1],[CylinderZ(0,3,100,3)])

# combine tool and coordinate axis = tool-assembly
finger1 = Collection([finger1,tooltip,xaxis,yaxis,zaxis])
finger1 = Translate([finger1],12.5,-20.0,-40)
finger1 = Rotate([finger1],-90,0,1,0)

try: # Expect files in working directory
    link7 = AsciiOBJ(filename="models/meca500_link7.obj")
    link6 = AsciiOBJ(filename="models/meca500_link6.obj")
    link5 = AsciiOBJ(filename="models/meca500_link5.obj")
    link4 = AsciiOBJ(filename="models/meca500_link4.obj")
    link3 = AsciiOBJ(filename="models/meca500_link3.obj")
    link2 = AsciiOBJ(filename="models/meca500_link2.obj")
    link1 = AsciiOBJ(filename="models/meca500_link1.obj")
    table = AsciiOBJ(filename="models/meca500_table.obj")
except Exception as detail:
    print(detail)
    raise SystemExit("meca500 requires files in models directory")

### Create link7
link7 = Color([0.9,0.9,0.9,1],[link7])
link7 = Collection([finger1, link7])
link7 = HalRotate([link7],c,"joint6",1,1,0,0)

### Create link6
link6 = Color([0.9,0.9,0.9,1],[link6])
link6 = Collection([link7, link6])
link6 = Translate([link6], 0,0,61)
link6 = HalRotate([link6],c,"joint5",1,0,1,0)

### Create link5
link5 = Color([0.9,0.9,0.9,1],[link5])
link5 = Collection([link6, link5])
link5 = Translate([link5], 0,0,61)
link5 = HalRotate([link5],c,"joint4",1,1,0,0)

### Create link4
link4 = Color([0.9,0.9,0.9,1],[link4])
link4 = Collection([link5, link4])
link4 = Translate([link4], -38.0,0,61.0)
link4 = Rotate([link4],90,0,1,0)
link4 = HalRotate([link4],c,"joint3",1,0,1,0)

### Create link3
link3 = Color([0.9,0.9,0.9,1],[link3])
link3 = Collection([link4, link3])
link3 = Translate([link3], 0,0,135.0)
link3 = HalRotate([link3],c,"joint2",1,0,1,0)

### Create link2
link2 = Color([0.9,0.9,0.9,1],[link2])
link2 = Collection([link3, link2])
link2 = Translate([link2], 0,0,135.0)
link2 = HalRotate([link2],c,"joint1",1,0,0,1)

### Create link1 stationary base
link1 = Color([0.9,0.9,0.9,1],[link1])
link1 = Translate([link1], 0,0,91)
meca500 = Collection([link2, link1])

# create visual world coordinates
xaxis0 = Color([1,0,0,1],[CylinderX(0,5,200,5)])
yaxis0 = Color([0,1,0,1],[CylinderY(0,5,200,5)])
zaxis0 = Color([0,0,1,1],[CylinderZ(0,5,200,5)])
coordw = Collection([xaxis0,yaxis0,zaxis0])

# create machine table
table = Color([0.9,0.9,0.9,1],[table])
table = Collection([table,coordw])
model = Collection([tooltip, meca500, table, work])

main(model, tooltip, work, 600, 600, None, -75, 300)
