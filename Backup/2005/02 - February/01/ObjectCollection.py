class ObjectCollection:
    """Holds objects, gives out handles, and can be used to look up handles."""

    def __init__(self):
        """Prepare the object collection to hold stuff."""

        self.nextID = 1
        self.objects = {}

    def addObject(self, newObject):
        """Add an object to the collection and return a handle."""

        self.objects[nextID] = newObject
        self.nextID = self.nextID + 1

        return self.nextID - 1

    def deleteObject(self, objectHandle):
        """Remove an object from the collection."""

        del self.objects[objectHandle]

    def clearCollection(self):
        """Remove EVERYTHING from the collection."""

        self.objects.clear()

    def checkHandle(self, objectHandle):
        """Check to see if the handle is valid."""

        return self.objects.has_key[objectHandle]

    def retrieveObject(self, objectHandle):
        """Return the object for the given handle."""

        if self.objects.has_key(objectHandle):
            return self.objects[objectHandle]
        else:
            return None

    def retrieveAllInClass(self, classHandle):
        """Retrieve all objects in a class."""

        if len(self.objects) == 0:
            return None

        if classHandle == None:
            return self.objects.values()

        self.objectsInClass = []

        for object in self.objects.values():
            if object.getClass() == classHandle:
                self.objectsInClass.append(object)

        return self.objectsInClass

    def retrieveAllInSubclass(self, classHandle, subclassHandle):
        """Retrieve all objects in a subclass."""

        if len(self.objects) == 0:
            return None

        if classHandle == None:
            return self.objects.values()

        self.objectsInClass = self.retrieveAllInClass(classHandle)

        if subclassHandle == None:
            return self.objectsInClass
        
        self.objectsInSubclass = []

        if self.objectsInClass == None:
            return None
        if len(self.objectsInClass) == 0:
            return None

        for object in self.objectsInClass:
            if object.getSubclass() == subclassHandle):
                self.objectsInSubclass.append(object)

        return self.objectsInSubclass
