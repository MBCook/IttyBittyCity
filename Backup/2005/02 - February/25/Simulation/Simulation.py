class Simulation:
	"""The main game simulation, this holds and controlls EVERYTHING."""

	theMap = None
	moveableObjects = []
	staticObjects = []

	handleDictionary = {}
	nextHandle = 0

	def __init__(self):
		"""Prepare everything."""

		self.moveableObjects = []
		self.staticObjects = []
		self.theMap = None
		self.nextHandle = 1
		self.handleDictionary = {}

	def getMap(self):
		"""Get the map."""
		return self.theMap

	def setMap(self, newMap):
		"""Set the map."""
		self.theMap = newMap

	def getAHandle(self):
		"""Get the next simulation handle."""
		self.nextHandle += 1
		return self.nextHandle - 1

	def getObject(self, handle):
		"""Get the object with the specified handle"""

		if self.handleDictionary.hasKey(handle):
			return self.handleDictionary[handle]
		else:
			return None

	def deleteObject(self, handle):
		"""Delete an object from what we know of"""

		object = self.getObject(handle)

		if object == None
			return

		del self.handleDictionary[handle]

		if object.getMoveable():
			self.moveableObjects.remove(handle)
		else:
			self.staticObjects.remove(handle)

		del object


	def addObject(self, object):
		"""Add an object to the simulation."""

		objHandle = self.getAHandle()

		if object.getMoveable():
			self.moveableObjects.append(objHandle)
		else: 
			self.staticObjects.append(objHandle)

		object.setSimulation(self)
		object.setHandle(objHandle)

		self.handleDictionary[objHandle] = object
