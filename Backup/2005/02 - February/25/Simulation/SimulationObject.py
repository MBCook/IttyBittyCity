import math

class SimulationObject:
	"""An object in the simulation."""

	className = None
	subclassName = None

	xPosition = 0.0
	yPosition = 0.0
	zPosition = 0.0
	width = 0.0
	height = 0.0
	depth = 0.0
	velocity = 0.0
	angle = 0.0
	angularVelocity = 0.0
	idealAngle = 0.0
	moveable = False
	collideable = False
	simulationHandle = None
	myHandle = None
	drawableHandle = None
	objectClassHandle = None
	objectSubclassHandle = None
	textureHandle = None

	def __init__(self):
		"""Initialiazed things with default values"""

		self.xPosition = 0.0
		self.yPosition = 0.0
		self.zPosition = 0.0
		self.width = 0.0
		self.height = 0.0
		self.depth = 0.0
		self.velocity = 0.0
		self.angle = 0.0
		self.angularVelocity = 0.0
		idealAngle = 0.0
		self.moveable = False
		self.simulationHandle = None
		self.drawableHandle = None
		self.textureHandle = None
		self.objectClassHandle = None
		self.objectSubclassHandle = None
		self.className = None
		self.subclassName = None
		self.myHandle = None

	def getSimulation(self):
		"""Get the simulation object."""
		return self.simulationHandle

	def setSimulation(self, simulation):
		"""Set the simulation handle."""
		self.simulationHandle = simulation

	def getCollideable(self):
		"""Get whether this object is subject to collisions."""
		return self.collideable

	def setCollideable(self, newSetting):
		"""Set whether this object is subject to collisions."""
		self.collideable = newSetting

	def getAngle(self):
		"""Get the object's angle."""
		return self.angle

	def setAngle(self, newAngle):
		"""Set the object's angle."""
		self.angle = newAngle

	def getHandle(self):
		"""Get this object's handle."""
		return self.myHandle

	def setHandle(self, newHandle):
		"""Set this object's handle."""
		self.myHandle = newHandle

	def getVelocity(self):
		"""Get the velocity of the object."""
		return self.velocity

	def setVelocity(self, newVelocity):
		"""Set the object's velocity."""
		self.velocity = newVelocity

	def getIdealAngle(self):
		"""Get the angular velocity of the object."""
		return self.idealAngle

	def setIdealAngle(self, newAngle):
		"""Set the angular velocity."""
		self.idealAngle = newAngle

	def getDrawable(self):
		"""Return the drawable handle."""
		return self.drawableHandle

	def setDrawable(self, newHandle):
		"""Set the drawable handle."""
		self.drawableHandle = newHandle

	def getTexture(self):
		"""Return texture handle."""
		return self.textureHandle

	def setTexture(self, newHandle):
		"""Set the texture handle."""
		self.textureHandle = newHandle

	def getPosition(self):
		"""Return a tuple of the object's position."""
		return (self.xPosition, self.yPosition, self.zPosition)

	def setPosition(self, x, y, z):
		"""Set the object's position."""

		self.xPosition = x
		self.yPosition = y
		self.zPosition = z

	def setXYPosition(self, x, y):
		"""Set the object's X and Y positions."""

		self.xPosition = x
		self.yPosition = y

	def setZPosition(self, z):
		"""Set the object's Z position."""
		self.zPosition = z

	def getSize(self):
		"""Return a tuple of the object's size."""
		return (self.width, self.height, self.depth)

	def setSize(self, w, h, d):
		"""Set the object's size."""

		self.width = w
		self.height = h
		self.depth = d

	def getMoveable(self):
		"""Return if the object is moveable or not."""
		return self.moveable

	def setMoveable(self, canMove):
		"""Set the moveable property of the object."""
		self.moveable = canMove

	def setObjectClass(self, handle):
		"""Set the class handle."""
		self.objectClassHandle = handle

	def setObjectSubclass(self, handle):
		"""Set the subclass handle."""
		self.objectSubclassHandle = handle

	def getClass(self):
		"""Get the class of this object."""
		return self.objectClassHandle

	def getSubclass(self):
		"""Get the subclass of this object."""
		return self.objectSubclassHandle

	def getAngluarVelocity(self):
		"""Get the angular velocity of our object."""
		return self.angularVelocity

	def setAngularVelocity(self, newAngular):
		"""Set the angular velocity of our object."""
		self.angularVelocity = newAngular

	def moveObject(self, time):
		"""Move the object in the world (if appropriate)."""
		if self.moveable:
			self.xPosition += time * self.velocity * math.cos(math.radians(self.angle))
			self.yPosition += time * self.velocity * math.sin(math.radians(self.angle))
			
			if self.angle == self.idealAngle):
				pass
			else:
				if ((self.angle >= self.idealAngle - 5.0) and (self.angle <= self.idealAngle + 5.0)):
					self.angle = self.idealAngle:
				elif self.angle < self.idealAngle:
					self.angle += time * self.angularVelocity
				else:
					self.angle -= time * self.angularVelocity
			
			if (self.angle < 0.0):
				self.angle += 360.0
			elif (self.angle >= 360.0):
				self.angle -= 360.0

	def recalcVelocity(self):
		"""Stub function to be used by subclasses if needed."""
		return

	def draw(self):
		"""Stub function to be used by subclasses if needed."""
