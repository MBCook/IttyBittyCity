class ObjectCollection:
    """Holds objects, gives out handles, and can be used to look up handles."""

    def __init__(self):
        """Prepare the object collection to hold stuff."""

        nextID = 1
        objects = {}

    def addObject(self, newObject):
        """Add an object to the collection and return a handle."""

        objects[nextID] = newObject
        nextID = nextID + 1

        return nextID - 1

    def deleteObject(self, objectHandle):
        """Remove an object from the collection."""

        del objects[objectHandle]

    def clearCollection(self):
        """Remove EVERYTHING from the collection."""

        objects.clear()

    def checkHandle(self, objectHandle):
        """Check to see if the handle is valid."""

        return objects.has_key[objectHandle]

    def retrieveObject(self, objectHandle):
        """Return the object for the given handle."""

        if objects.has_key(objectHandle):
            return objects[objectHandle]
        else:
            return None

    def retrieveAllInClass(self, classHandle):
        """Retrieve all objects in a class."""

        if len(objects) == 0:
            return None

        if classHandle == None:
            return objects.values()

        objectsInClass = []

        for object in objects.values():
            if object.getClass() == classHandle:
                objectsInClass.append(object)

        return objectsInClass

    def retrieveAllInSubclass(self, classHandle, subclassHandle):
        """Retrieve all objects in a subclass."""

        if len(objects) == 0:
            return None

        if classHandle == None:
            return objects.values()

        objectsInClass = self.retrieveAllInClass(classHandle)

        if subclassHandle == None:
            return objectsInClass
        
        objectsInSubclass = []

        if objectsInClass == None:
            return None
        if len(objectsInClass) == 0:
            return None

        for object in objectsInClass:
            if object.getSubclass() == subclassHandle):
                objectsInSubclass.append(object)

        return objectsInSubclass
