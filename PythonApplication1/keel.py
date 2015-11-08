# This is a CadQuery script template
# Add your script code below

import sys
sys.path.append('/c/Program Files (x86)/FreeCAD 0.14/bin')
sys.path.append('/c/Program Files (x86)/FreeCAD 0.14/lib')
from cadquery import *
import cadquery

from Helpers import show

# Use the following to render your model with grey RGB and no transparency
# show(my_model, (204, 204, 204, 0.0))

result = cadquery.Workplane("front").box(4.0, 4.0, 0.25).faces(">Z") \
                 .circle(1.5).workplane(offset=3.0) \
                 .rect(0.75, 0.5).loft(combine=True)


#keelstock = Workplane("XY").workplane(offset=(50)).box(7,4,50)
keelstock = Workplane("XY").box(7,4,50).faces(">Z").rect(1,4).extrude(-50)
#.workplane(offset=-50)                 .rect(0.75, 0.5).extrude(0.5)

show(keelstock)
