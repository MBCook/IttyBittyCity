from SimulationObject import *
import car_video
import VideoRoutines
import pathfinder
import math
import map_to_points

class Car(SimulationObject):
	"""Our little car class."""

	accelerationPercent = 0.0
	accelerationMax = 2.0
	brakePercent = 0.0
	brakeMax = 1.0
	currentNode = ""
	goalNode = ""
	pathToGoal = ""
	currentTarget = ""

	def __init__(self):
		"""Initialize everything."""

		textureFile = "Objects/Car/car_texture.png"

		SimulationObject.__init__(self) # Initialize base class stuff

		self.className = "Vehicles"
		self.subclassName = "Car"
		self.moveable = True

		self.drawableHandle = car_video.makeDisplayList()

		tempHandle = VideoRoutines.getTexture(textureFile)

		if tempHandle:
			self.textureHandle = tempHandle
		else:
			self.textureHandle = VideoRoutines.loadTexture(textureFile, False)

		self.currentNode = ""
		self.goalNode = ""
		self.pathToGoal = []
		self.currentTarget = ""

	def getGoalNode(self):
		"""Get the current goal node."""
		return self.goalNode

	def setGoalNode(self, newGoal):
		"""Set a new goal node."""
		self.goalNode = newGoal

	def getCurrentTarget(self):
		"""Get the current target of this object."""
		return self.currentTarget

	def getCurrentNode(self):
		"""Get the current node (the one we're closest to)."""
		return self.currentNode

	def calculateNewPath(self):
		"""Get a new path for us to follow."""

		nodeDict = self.simulationHandle.getMap().getNodeDict()
		distDict = self.simulationHandle.getMap().getDistDict()

		self.path = pathfinder.findPath(self.currentNode, self.goalNode, nodeDict, distDict)

	def getNextTarget(self):
		"""Set the current target to the next node along the path."""

		if self.path == []:
			self.decideOnGoal()
			self.calculateNewPath()
	
		self.currentTarget = self.path.pop(0)		

	def draw(self):
		"""Draw this object."""

		car_video.drawMe(self)

	def decideOnGoal(self):
		"""Decided on what our next goal will be."""

		self.goalNode = self.simulationHandle.getMap().getRandomNode()

	def moveObject(self, time):
		"""Move the car."""

		nodeDict = self.simulationHandle.getMap().getNodeDict()

		# First we get ourselves a goal

		if self.currentNode = self.goalNode:
			self.getNextTarget()

		currentX, currentY = map_to_points.getCoords(self.currentTarget, nodeDict)

		xDiff = currentX - self.xPosition
		yDiff = currentY - self.yPosition

		dist = math.sqrt(math.pow(xDiff, 2) + math.pow(yDiff, 2))

		angleToTarget = math.atan2(yDiff, xDiff)
		angleToTarget = math.degrees(angleToTarget)

		self.idealAngle = angleToTarget

		if dist < 0.2:
			self.currentNode = self.currentTarget
			self.getNextTarget()

		# Then we let the default moveObject move us

		SimulationObject.moveObject(self, time)