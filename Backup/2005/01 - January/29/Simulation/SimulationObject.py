import math

class SimulationObject:
    """An object in the simulation."""

    def __init__(self):
        """Initialiazed things with default values"""

        xPosition = 0.0
        yPosition = 0.0
        zPosition = 0.0
        width = 0.0
        height = 0.0
        depth = 0.0
        velocity = 0.0
        angle = 0.0
        angularVelocity = 0.0
        moveable = False
        simulationHandle = None
        drawableHandle = None
        objectClassHandle = None
        objectSubclassHandle = None

    def getHandle(self):
        """Get this object's handle."""
        return simulationHandle

    def setHandle(self, newHandle):
        """Set this object's handle."""
        simulationHandle = newHandle

    def getVelocity(self):
        """Get the velocity of the object."""
        return velocity

    def setVelocity(self, newVelocity):
        """Set the object's velocity."""
        velocity = newVelocity

    def getAngularVelocity(self):
        """Get the angular velocity of the object."""
        return angularVelocity

    def setAngularVelocity(self, newAngular):
        """Set the angular velocity."""
        angularVelocity = newAngular

    def getPosition(self):
        """Return a tuple of the object's position."""
        return (xPosition, yPosition, zPosition)

    def setPosition(self, x, y, z):
        """Set the object's position."""

        xPosition = x
        yPosition = y
        zPosition = z

    def setXYPosition(self, x, y):
        """Set the object's X and Y positions."""

        xPosition = x
        yPosition = y

    def setZPosition(self, z):
        """Set the object's Z position."""
        zPosition = z

    def getSize(self):
        """Return a tuple of the object's size."""
        return (width, height, depth)

    def setSize(self, w, h, d):
        """Set the object's size."""

        width = w
        height = h
        depth = d

    def getMoveable(self):
        """Return if the object is moveable or not."""
        return moveable

    def setMoveable(self, canMove):
        """Set the moveable property of the object."""
        moveable = canMove

    def getDrawable(self):
        """Return the drawable handle."""
        return drawableHandle

    def setDrawable(self, handle):
        """Set the drawable handle."""
        drawableHandle = handle

    def setObjectClass(self, handle):
        """Set the class handle."""
        objectClassHandle = handle

    def setObjectSubclass(self, handle):
        """Set the subclass handle."""
        objectSubclassHandle = handle

    def getClass(self):
        """Get the class of this object."""
        return objectClassHandle

    def getSubclass(self):
        """Get the subclass of this object."""
        return objectSubclassHandle

    def moveObject(self, time):
        """Move the object in the world (if appropriate)."""
        if moveable:
            xPosition += time * velocity * math.cos(math.radians(angle))
            yPosition += time * velocity * math.sin(math.radians(angle))
            angle += time * angularVelocity
            if (angle < 0.0)
                angle += 360.0
            elif (angle >= 360.0)
                angle -= 360.0`

    def recalcVelocity(self):
        """Stub function to be used by subclasses if needed."""
        return
