import Road
import random

class Map:
	"""A map for use in our simulation."""

	mapData = []
	width = 0
	height = 0
	nodeDict = {}
	distDict = {}

	mapObjects = []

	def __init__(self):
		"""Prepare the map with no data."""

		self.mapData = []
		self.width = 0
		self.height = 0
		self.nodeDict = {}
		self.distDict = {}

	def loadMapData(self, data, w, h, nDict, dDict):
		"""Load data into our map."""

		self.mapData = data
		self.width = w
		self.height = h
		self.nodeDict = nDict
		self.distDict = dDict

	def getNodeDict(self):
		"""Return the node dictionary."""
		return self.nodeDict

	def getDistDict(self):
		"""Return the distance dictionary."""
		return self.distDict

	def getRandomNode(self):
		"""Get a random node."""

		nodeList = self.nodeDict.keys()

		random.seed()

		return random.choice(nodeList)

	def setupObjects(self):
		"""Get all the road tiles ready."""

		for y in range(self.height):
			for x in range(self.width):
				tempType = self.getSquare(x, y)
				if tempType <= 11:
					xCoord = float(x)
					yCoord = float(y)
					tempObject = Road.Road(tempType)
					tempObject.setPosition(xCoord * 12.0, (float(self.height) - yCoord) * 12.0, 0.0)
					self.mapObjects.append(tempObject)

	def draw(self):
		"""Draw the map"""

		# Note that the lower left corner of the map is at the origin.

		for o in self.mapObjects:
			o.draw()

	def getSquare(self, x, y):
		"""Find out what is at square x,y."""

		if ((x < 0) or (x >= self.width) or (y < 0) or (y >= self.height)):
			raise NameError, "Bad coords: %d,%d" % (x, y)

		return self.mapData[x + y * self.width]

	def getWidth(self):
		"""Get the map width."""
		return self.width

	def getHeight(self):
		"""Get the map height."""
		return self.height
