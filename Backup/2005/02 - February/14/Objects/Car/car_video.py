from OpenGL.GL import *
from OpenGL.GLU import *
from VideoRoutines import *
import pygame

def drawMe(self):
	"""Draw this object."""

	glPushMatrix()
	glLoadIdentity()

	if self.angle > 0.0:
		glRotatef(self.angle, 0.0, 0.0, 1.0)

	glTranslatef(self.xPosition, self.yPosition, self.zPosition)

	glBindTexture(GL_TEXTURE_2D, self.textureHandle)
	glCallList(self.drawableHandle)

	glPopMatrix()

def loadTexture(file):
	"""Load a texture."""

	texHan = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, texHan)

	# Setup some OpenGL stuff

	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

	# Load the image

	textureSurface = pygame.image.load(file)

	# Put it into a string for OpenGL

	dataString = pygame.image.tostring(textureSurface, "RGBA", 0)

	# Now lets give that to OpenGL

	gluBuild2DMipmaps(GL_TEXTURE_2D, 4, 256, 256, GL_RGBA, GL_BYTE, dataString)

	return texHan

def makeDisplayList(num = 0):
	"""This makes a display list containing our car."""

	# First we have to get all the vertex data out of the car_data.py file
	# This uses some magic in the form of the built in function "execfile".
	# We have to do this because otherwise Python doesn't like the formulas in
	#	the list.

	car_dict = {}

	execfile("Objects/Car/car_data.py", car_dict)

	# OK, if that worked, we have everything we need in car_dict
	# So now we run the function in the file

	makeCarData = car_dict['makeCarData']

	body_data, tire_data = makeCarData()

	if ((num == 0) or (num == None)):
		# We don't have a display list, get one
		carDisplayList = glGenLists(1)
	else:
		# Use the one we already have
		carDisplayList = num

	if carDisplayList == 0:
		raise NameError, "Given bad display list number (0)."

	# Star the list

	glLoadIdentity()

	glNewList(carDisplayList, GL_COMPILE)

	# Draw the car centered at the origin (with wheels touching XY plane)

	glTranslatef(-2.0, -4.25, 0.0)

	# Draw things!

	drawFromArray(body_data, True)

	glPushMatrix()
	glTranslatef(0.75, 1.5, 0.0)
	drawFromArray(tire_data, False)
	glPopMatrix()

	glPushMatrix()
	glTranslatef(0.75, 6.5, 0.0)
	drawFromArray(tire_data, False)
	glPopMatrix()

	glPushMatrix()
	glTranslatef(3.25, 1.5, 0.0)
	drawFromArray(tire_data, False)
	glPopMatrix()

	glPushMatrix()
	glTranslatef(3.25, 6.5, 0.0)
	drawFromArray(tire_data, False)
	glPopMatrix()

	# Done!

	glEndList()

	# Return the display list number

	return carDisplayList