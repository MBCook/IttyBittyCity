from OpenGL.GL import *
from SimulationObject import *
from VideoRoutines import *

class Ground(SimulationObject):
	"""The ground. Very simple test class."""

	def __init__(self):
		"""Init things."""

		SimulationObject.__init__(self)

		self.className = "Ground"
		self.subclassname = "Dirt"

		self.collideable = False

		self.setSize(25.0, 25.0)

	def draw(self):
		"""Draw this object."""

		glDisable(GL_TEXTURE_2D)

		glPushMatrix()
		glLoadIdentity()

		glTranslatef(self.xPosition, self.yPosition, self.zPosition)

		if self.angle > 0.0:
			glRotatef(self.angle, 0.0, 0.0, 1.0)

		glCallList(self.drawableHandle)

		glPopMatrix()

		glEnable(GL_TEXTURE_2D)

	def setSize(self, w, h):
		"""Create the ground at the specified size."""

		self.width = w
		self.height = h

		# Now the color of the ground

		gRed = 75.0 / 255.0
		gGreen = 62.0 / 255.0
		gBlue = 56.0 / 255.0

		arrayData = [
			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			-w/2.0, h/2.0, 0.0,

			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			-w/2.0, -h/2.0, 0.0,

			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			w/2.0, h/2.0, 0.0,

			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			-w/2.0, -h/2.0, 0.0,

			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			w/2.0, -h/2.0, 0.0,

			gRed, gGreen, gBlue, 1.0,
			0.0, 0.0, 1.0,
			w/2.0, h/2.0, 0.0]

		# Now that we have the data, we make our display list.

		displayListNum = glGenLists(1)

		if displayListNum == 0:
			raise NameError, "Given bad display list number (0)."

		glNewList(displayListNum, GL_COMPILE)

		drawFromArray(arrayData, False)

		glEndList()
		
		self.drawableHandle = displayListNum
