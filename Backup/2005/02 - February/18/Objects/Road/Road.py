from OpenGL.GL import *
from SimulationObject import *
from VideoRoutines import *

class Road(SimulationObject):
	"""The ground. Very simple test class."""

	roadType = None

	def __init__(self, type):
		"""Init things."""

		SimulationObject.__init__(self)

		self.className = "Road"
		self.roadType = type

		if type == 0:
			self.subclassname = "Grass"
			self.setSize(12.0, 12.0)
		elif type == 1:
			self.subclassname = "Horizontal"
			self.setSize(12.0, 12.0)
		elif type == 2:
			self.subclassname = "Virticle"
			self.angle = 90.0
			self.setSize(12.0, 12.0)
		elif type == 3:
			self.subclassname = "Intersection"
			self.setSize(12.0, 12.0)
		elif type == 4:
			self.subclassname = "T Down"
			self.setSize(12.0, 12.0)
		elif type == 5:
			self.subclassname = "T Left"
			self.angle = 270.0
			self.setSize(12.0, 12.0)
		elif type == 6:
			self.subclassname = "T Up"
			self.angle = 180.0
			self.setSize(12.0, 12.0)
		elif type == 7:
			self.subclassname = "T Right"
			self.angle = 90.0
			self.setSize(12.0, 12.0)
		elif type == 8:
			self.subclassname = "Curve BR"
			self.setSize(24.0, 24.0)
		elif type == 9:
			self.subclassname = "Curbe BL"
			self.setSize(24.0, 24.0)
			self.angle = 270.0
		elif type == 10:
			self.subclassname = "Curve TL"
			self.setSize(24.0, 24.0)
			self.angle = 180.0
		elif type == 11:
			self.subclassname = "Curve TR"
			self.setSize(24.0, 24.0)
			self.angle = 90.0
		else:
			raise NameError, "Unknown road type passed: %d" % type

		self.collideable = False

		textureFile = "Objects/Road/Road.png"
		tempHandle = getTexture(textureFile)

		if tempHandle > 0:
			self.textureHandle = tempHandle
		else:
			self.textureHandle = loadTexture(textureFile, False)

	def draw(self):
		"""Draw this object."""

		glPushMatrix()
		glLoadIdentity()

		if self.angle > 0.0:
			glRotatef(self.angle, 0.0, 0.0, 1.0)

		glTranslatef(-self.xPosition, -self.yPosition, -self.zPosition)

		glBindTexture(GL_TEXTURE_2D, self.textureHandle)
		glCallList(self.drawableHandle)

		glPopMatrix()

	def setSize(self, w, h):
		"""Create the ground at the specified size."""

		self.width = w
		self.height = h

		tw = 0.25
		th = 0.25

		if (self.roadType >= 8) and (self.roadType <= 11):
			tsx = 0.5
			tsy = 0.25
			tw = 0.50
			th = 0.50
		elif (self.roadType >= 4) and (self.roadType <= 7):
			tsx = 0.5
			tsy = 0.0
		else:
			tsy = 0.0
			if self.roadType == 0:
				tsx = 0.75
			elif (self.roadType == 1) or (self.roadType == 2):
				tsx = 0.0
			elif self.roadType == 3:
				tsx = 0.5

		# Now the color of the road

		gRed = 1.0
		gGreen = 1.0
		gBlue = 1.0

		arrayData = [
			tsx, tsy,
			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			-w/2.0, h/2.0, 0.0,

			tsx, tsy + th,
			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			-w/2.0, -h/2.0, 0.0,

			tsx + tw, tsy,
			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			w/2.0, h/2.0, 0.0,

			tsx, tsy + th,
			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			-w/2.0, -h/2.0, 0.0,

			tsx + tw, tsy + th,
			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			w/2.0, -h/2.0, 0.0,

			tsx + tw, tsy,
			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			w/2.0, h/2.0, 0.0]

		# Now that we have the data, we make our display list.

		displayListNum = glGenLists(1)

		if displayListNum == 0:
			raise NameError, "Given bad display list number (0)."

		glNewList(displayListNum, GL_COMPILE)

		drawFromArray(arrayData, True)

		glEndList()
		
		self.drawableHandle = displayListNum
