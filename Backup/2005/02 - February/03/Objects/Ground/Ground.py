from OpenGL.GL import *
from SimulationObject import *
from VideoHelper import *

class Ground(SimulationObject):
    """The ground. Very simple test class."""

    def __init__(self):
        """Init things."""

        SimulationObject(self)

        self.className = "Ground"
        self.subclassname = "Dirt"

        self.collideable = False

        self.setSize(25.0, 25.0)

    def setSize(self, w, h):
        """Create the ground at the specified size."""

        self.width = w
        self.height = h

        # Now the color of the ground

        gRed = 125.0 / 255.0
        gGreen = 42.0 / 255.0
        gBlue = 56.0 / 255.0

        arrayData = [
            gRed, gGreen, gBlue, 1.0,
            0.0, 0.0, 1.0,
            -w/2.0, h/2.0, 0.0,

            gRed, gGreen, gBlue, 1.0,
            0.0, 0.0, 1.0,
            -w/2.0, -h/2.0, 0.0,

            gRed, gGreen, gBlue, 1.0,
            0.0, 0.0, 1.0,
            w/2.0, h/2.0, 0.0,

            gRed, gGreen, gBlue, 1.0,
            0.0, 0.0, 1.0,
            -w/2.0, -h/2.0, 0.0,

            gRed, gGreen, gBlue, 1.0,
            0.0, 0.0, 1.0,
            w/2.0, -h/2.0, 0.0,

            gRed, gGreen, gBlue, 1.0,
            0.0, 0.0, 1.0,
            w/2.0, h/2.0, 0.0]

        # Now that we have the data, we make our display list.

        displayListNum = glGenLists(1)

        if displayListNum == 0:
            except NameError, "Given bad display list number (0)."

        glNewList(displayListNum, GL_COMPILE)

        drawFromArray(arrayData, 4)

        glEndList()
        
        self.drawableHandle = displayListNum
