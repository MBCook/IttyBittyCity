from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

global textureCache

def initTextureCache():
	"""Prepare the texture cache"""

	global textureCache

	textureCache = {}

def getTexture(file):
	"""Get a texture handle"""

	global textureCache

	if textureCache.has_key(file):
		return texHan[file]
	else:
		return 0

def loadTexture(file, transparent = False):
	"""Load a texture."""

	global textureCache

	# Load the image

	textureSurface = pygame.image.load(file)

	# Reserve a texture

	texHan = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, texHan)

	# Setup some OpenGL stuff

	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

	# Put it into a string for OpenGL

	dataString = pygame.image.tostring(textureSurface, "RGBA", 0)

	# Now lets give that to OpenGL

	if transparent == False:
		gluBuild2DMipmaps(GL_TEXTURE_2D, 4, 256, 256, GL_RGBA, GL_UNSIGNED_BYTE, dataString)
	else:
		gluBuild2DMipmaps(GL_TEXTURE_2D, 4, 256, 256, GL_RGB, GL_UNSIGNED_BYTE, dataString)

	textureCache[file] = texHan

	return texHan

def drawFromArray(array, textured):
	"""Draw the triangles in the array. GL_T2F_C4F_N3F_V3F"""

	if textured:
		npt = 36				# Number of things per traingle
	else:
		npt = 30

	vC = len(array) / npt	# Veretex count
	npv = npt / 3			# Number of things per vertex

	glBegin(GL_TRIANGLES)

	if textured:
		for j in range(vC):
			for i in range(3):

				cV = j * npt + i * npv

				glTexCoord2f(array[cV], array[cV + 1])
				glColor4f(array[cV + 2], array[cV + 3],	array[cV + 4], array[cV + 5])
				glNormal3f(array[cV + 6], array[cV + 7], array[cV + 8])
				glVertex3f(array[cV + 9], array[cV + 10], array[cV + 11])

	else:
		for j in range(vC):
			for i in range(3):

				cV = j * npt + i * npv

				glColor4f(array[cV], array[cV + 1],	array[cV + 2], array[cV + 3])
				glNormal3f(array[cV + 4], array[cV + 5], array[cV + 6])
				glVertex3f(array[cV + 7], array[cV + 8], array[cV + 9])

	glEnd()

def drawNormalsFromArray(array, textured):
	"""Draw the normals to the polygons."""

	if textured:
		npt = 36
	else:
		npt = 30

	vC = len(array) / npt
	npv = npt / 3

	glBegin(GL_LINES)

	if textured:
		for j in range(vC):
			x = 0.0
			y = 0.0
			z = 0.0

			cV = j * npt

			nx = array[cV + 6]
			ny = array[cV + 7]
			nz = array[cV + 8]

			for i in range(3):
				cV = j * npt + i * npv
				x = x + array[cV + 9]
				y = y + array[cV + 10]
				z = z + array[cV + 11]

			x = x / 3.0
			y = y / 3.0
			z = z / 3.0

			glColor4f(0.0, 0.0, 0.0, 1.0)
			glVertex3f(x, y, z)
			glVertex3f(x + nx, y + ny, z + nz)

	else:
		for j in range(vC):
			x = 0.0
			y = 0.0
			z = 0.0

			cV = j * npt

			nx = array[cV + 4]
			ny = array[cV + 5]
			nz = array[cV + 6]

			for i in range(3):
				cV = j * npt + i * npv
				x = x + array[cV + 7]
				y = y + array[cV + 8]
				z = z + array[cV + 9]

			x = x / 3.0
			y = y / 3.0
			z = z / 3.0

			glColor4f(0.0, 0.0, 0.0, 1.0)
			glVertex3f(x, y, z)
			glVertex3f(x + nx, y + ny, z + nz)

	glEnd()
