class SimulationObject:
    """An object in the simulation."""

    def __init__(self):
        """Initialiazed things with default values"""

        xPosition = 0.0
        yPosition = 0.0
        zPosition = 0.0
        width = 0.0
        height = 0.0
        velocity = 0.0
        angle = 0.0
        moveable = False
        simulationHandle = None
        drawableHandle = None
        objectClassHandle = None
        objectSubclassHandle = None

    def getClass(self):
        """Get the class of this object."""
        return objectClassHandle

    def getSubclass(self):
        """Get the subclass of this object."""
        return objectSubclassHandle
