from SimulationObject import *
from car_video import *

class Car(SimulationObject):
	"""Our little car class."""

	accelerationPercent = 0.0
	accelerationMax = 2.0
	brakePercent = 0.0
	brakeMax = 1.0
	drawStyle = 0

	def __init__(self):
		"""Initialize everything."""

		SimulationObject.__init__(self) # Initialize base class stuff

		self.className = "Vehicles"
		self.subclassName = "Car"
		self.drawStyle = 0
		self.moveable = True

		self.setDrawStyle(4)	# Draw things normal by default

	def getDrawStyle(self):
		"""Get the current drawing style."""
		return self.drawStyle

	def setDrawStyle(self, style):
		"""Set the drawing style."""

		self.drawStyle = style
		displayList = makeDisplayList(style, self.drawableHandle)
		self.drawableHandle = displayList
