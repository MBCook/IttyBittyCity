from SimulationObject import *
import car_video

class Car(SimulationObject):
	"""Our little car class."""

	accelerationPercent = 0.0
	accelerationMax = 2.0
	brakePercent = 0.0
	brakeMax = 1.0

	def __init__(self):
		"""Initialize everything."""

		SimulationObject.__init__(self) # Initialize base class stuff

		self.className = "Vehicles"
		self.subclassName = "Car"
		self.moveable = True

		self.drawableHandle = car_video.makeDisplayList()
		self.textureHandle = car_video.loadTexture("Objects/Car/car_texture.png")

	def draw(self):
		"""Draw this object."""

		car_video.drawMe(self)
