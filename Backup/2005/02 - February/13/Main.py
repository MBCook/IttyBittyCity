import sys
import os

currentPath = sys.path[0]

pathA = os.path.join(currentPath, "Simulation")
pathB = os.path.join(currentPath, "Video")
pathC = os.path.join(currentPath, "Objects/Car")
pathD = os.path.join(currentPath, "Objects/Ground")

sys.path.append(pathA)
sys.path.append(pathB)
sys.path.append(pathC)
sys.path.append(pathD)

import Video
import Preferences
import pygame

# Temporary objects for testing

import Car
import Ground

from OpenGL.GL import *

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


def main():
	"""The main program."""

	# Initialize Pygame

	pygame.init()

	# First we set some stuff up.

	prefs = Preferences.Preferences()
	prefs.loadPreferences()
	video = Video.Video(prefs)
	video.prepareVideo()

	carObject = Car.Car()
	groundObject = Ground.Ground()

	carDir = 0.0

	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		carDir += 1.0
		if (carDir >= 360.0):
			carDir -= 360.0
		carObject.setAngle(carDir)

		video.prepareNewFrame()
		video.setupCamera()
		video.setupLights()

		# Drawing happens here

		glLoadIdentity()

		drawReference(0.0, 0.0, 0.0, 1.0)

		video.drawSimulationObject(groundObject)
		video.drawSimulationObject(carObject)

		video.finishNewFrame()

		pygame.time.wait(33)

if __name__ == "__main__":
	main()
