# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:04:04 2015

@author: hakon
"""
#from OCC.Display.SimpleGui import init_display
#from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox


import sys
#sys.path.append('/c/Program Files (x86)/FreeCAD 0.14/bin')
#sys.path.append('/c/Program Files (x86)/FreeCAD 0.14/lib')
from cadquery import *
import cadquery

# sys.path.insert(0, _fc_path())

from Helpers import show


import FreeCAD
import Part as FreeCADPart
# from cadquery.freecad_impl import *

def makeEllipseResearch(self, majorRadius, minorRadius):
    #self refers to the CQ or Workplane object

    #inner method that creates an ellipse
    def _singleEllipse(pnt):
        #pnt is a location in local coordinates
        #since we're using eachpoint with useLocalCoordinates=True
        #return Solid.makeBox(length,length,length,pnt)
        # Denne funker, maa wrappes
        o = FreeCADPart.Wire(FreeCADPart.makeCircle(1))
        w = Wire(o)

        o = FreeCADPart.Wire(FreeCADPart.Ellipse(FreeCAD.Base.Vector(10,0,0),FreeCAD.Base.Vector(0,5,0),FreeCAD.Base.Vector(0,0,0)).toShape())
        w = Wire(o)
        #o = FreeCADPart.makePolygon([FreeCAD.Base.Vector(0,5,0),FreeCAD.Base.Vector(0,0,0),FreeCAD.Base.Vector(5,0,0),FreeCAD.Base.Vector(5,5,0), FreeCAD.Base.Vector(0,5,0)])
        #w = Wire(o)
        w.forConstruction = False
        return w

    #use CQ utility method to iterate over the stack, call our
    #method, and convert to/from local coordinates.
    #retVal = CQ(Solid.makeBox(1.0,2.0,3.0))
    #retVal = CQ(Shape.cast(FreeCADPart.makeBox(1.0,2.0,3.0)))
    #obj = CQ(Shape.cast(FreeCADPart.Ellipse().toShape()))
    #retVal = obj.newObject(self.objects)
    #obj = Wire(FreeCADPart.Ellipse())

    retVal = self.eachpoint(_singleEllipse,True)

    #retVal = CQ(FreeCADPart.makeBox(1.0,2.0,3.0))
    #retVal = FreeCADPart.makeBox(1.0,2.0,3.0, pnt.wrapped, dir.wrapped)
    return retVal

def makeEllipse(self, majorRadius, minorRadius):
    #self refers to the CQ or Workplane object

    #inner method that creates an ellipse
    def _singleEllipse(pnt):
        #pnt is a location in local coordinates
        #since we're using eachpoint with useLocalCoordinates=True
        o = FreeCADPart.Wire(FreeCADPart.Ellipse(pnt.wrapped, majorRadius, minorRadius).toShape())
        # Must wrap
        w = Wire(o)
        w.forConstruction = False
        #obj = CQ(w)
        #retVal = obj.newObject(self.objects)
        #return retVal
        return w
    #use CQ utility method to iterate over the stack, call our
    retVal = self.eachpoint(_singleEllipse,True)

    #retVal = CQ(FreeCADPart.makeBox(1.0,2.0,3.0))
    #retVal = FreeCADPart.makeBox(1.0,2.0,3.0, pnt.wrapped, dir.wrapped)
    return retVal

def makeCubes(self,length):
    #self refers to the CQ or Workplane object

    #inner method that creates a cube
    def _singleCube(pnt):
        #pnt is a location in local coordinates
        #since we're using eachpoint with useLocalCoordinates=True
        return Solid.makeBox(length,length,length,pnt)

    #use CQ utility method to iterate over the stack, call our
    #method, and convert to/from local coordinates.
    return self.eachpoint(_singleCube,True)

#link the plugin into cadQuery
Workplane.makeCubes = makeCubes
Workplane.makeEllipse = makeEllipse

result = Workplane("front").box(4.0,4.0,0.25).faces(">Z").circle(1.5) \
     .workplane(offset=3.0).makeEllipse(2,1).loft(combine=True)

areblad = Workplane("XY").workplane(offset=(50)).box(10,1,50).rotateAboutCenter((0,0,0),90)
arehals = Workplane("XY").rect(1,10).workplane(offset=15).makeEllipse(2,1)
aarehals1 = Workplane("XY").workplane(offset=(50)).box(10,1,1)

bladhals = areblad.faces(">Z").rect(1,10). \
     workplane(offset=15).makeEllipse(2,1).loft(combine=True)

#h = areblad.faces(">Z").add(arehals).loft(combine=True)
oar = bladhals.faces(">Z").makeEllipse(2,1).workplane(offset=200).circle(3).loft(combine=True)
show(oar)
