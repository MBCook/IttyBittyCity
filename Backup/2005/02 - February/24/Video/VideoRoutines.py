from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import map_to_points

global textureCache

def drawReference(x, y, z, l):
    """Draw a little reference market"""

    glPushMatrix()

    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_LINES)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(x, y, z)
    glVertex3f(x + l, y, z)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_LINES)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(x, y, z)
    glVertex3f(x, y + l, z)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)

    glBegin(GL_LINES)
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(x, y, z)
    glVertex3f(x, y, z + l)
    glEnd()

    glPopMatrix()

def initTextureCache():
	"""Prepare the texture cache"""

	global textureCache

	textureCache = {}

def getTexture(file):
	"""Get a texture handle"""

	global textureCache

	if textureCache.has_key(file):
		return textureCache[file]
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

def drawPathsPrep(nodeDict, distanceDict):
	"""Make the lists we'll need for drawing everything."""
	
	lines = []
	points = []

#	i = 5

	keyList = distanceDict.keys()
	keyList.sort()

	for key in keyList:
#		i = i - 1
#		if i == 0:
#			break
		nodeA = key[0:6]
		nodeB = key[6:12]
		tupleA = map_to_points.getCoords(nodeA, nodeDict)
		tupleB = map_to_points.getCoords(nodeB, nodeDict)

		(x, y) = tupleA
		(x2, y2) = tupleB

#		print "%s: (%f, %f) and (%f, %f, %f, %f)" % (key, x, y, x, y, x2, y2)

		points.extend([x, y, x2, y2])

		lines.extend([x, y, x2, y2])

	return (points, lines)

def drawPaths(points, lines, height, lineWidth, pointRadius):
	"""Extract connections from the distance database and draw some lines!"""

	lineArraySize = len(lines)
	pointArraySize = len(points)
	lineArrayItems = lineArraySize / 4
	pointArrayItems = pointArraySize / 2


	glLineWidth(lineWidth)
	glPointSize(pointRadius)

	glColor4f(0.0, 0.0, 1.0, 1.0)
	glNormal3f(0.0, 0.0, 1.0)

	glDisable(GL_TEXTURE_2D)

	glBegin(GL_LINES)

#	glLoadIdentity()

	for i in range(lineArrayItems):
		glVertex3f(lines[i * 4], height - lines[i * 4 + 1], 0.1)
		glVertex3f(lines[i * 4 + 2], height - lines[i * 4 + 3], 0.1)

	glEnd()

	glBegin(GL_POINTS)

#	glLoadIdentity()

	for i in range(pointArrayItems):
		glVertex3f(points[i * 2], height - points[i * 2 + 1], 0.11)

	glEnd()

	glEnable(GL_TEXTURE_2D)
