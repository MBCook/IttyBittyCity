from SimulationObject import *
import car_video
import VideoRoutines

class Car(SimulationObject):
	"""Our little car class."""

	accelerationPercent = 0.0
	accelerationMax = 2.0
	brakePercent = 0.0
	brakeMax = 1.0

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

	def draw(self):
		"""Draw this object."""

		car_video.drawMe(self)
