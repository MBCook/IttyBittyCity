import sys
import os

currentPath = sys.path[0]

pathA = os.path.join(currentPath, "Simulation")
pathB = os.path.join(currentPath, "Video")
pathC = os.path.join(currentPath, "Objects/Car")
pathD = os.path.join(currentPath, "Objects/Ground")
pathE = os.path.join(currentPath, "Objects/Road")
pathF = os.path.join(currentPath, "Objects/Map")

sys.path.append(pathA)
sys.path.append(pathB)
sys.path.append(pathC)
sys.path.append(pathD)
sys.path.append(pathE)
sys.path.append(pathF)

import Video
import Preferences
import pygame
import VideoRoutines
import Car
import Ground
import Road
import Map
import test_map
import pickle

from OpenGL.GL import *

def main():
	"""The main program."""

	# Initialize Pygame

	print "Starting Pygame..."

	pygame.init()

	# First we set some stuff up.

	print "Initializing stuff..."

	prefs = Preferences.Preferences()
	prefs.loadPreferences()
	video = Video.Video(prefs)
	video.prepareVideo()

	carObject = Car.Car()
	groundObject = Map.Map()

	groundObject.loadMapData(test_map.t_d, test_map.t_w, test_map.t_h)
	groundObject.setupObjects()

	carObject.setXYPosition(8.0, 9.0)

	carDir = 0.0

	print "Unpickleing dictionaries..."

	nodeFile = open("Objects/Map/node_list.dat", "r")
	distFile = open("Objects/Map/node_distances.dat", "r")

	nodeDict = pickle.load(nodeFile)
	distDict = pickle.load(distFile)

	nodeFile.close()
	distFile.close()

	# Now we do things

	print "Preparing lists for drawing paths..."

	(points, lines) = VideoRoutines.drawPathsPrep(nodeDict, distDict)

	print "Starting main loop..."

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

		groundObject.draw()
		carObject.draw()

		glLoadIdentity()

		VideoRoutines.drawPaths(points, lines, 20.0, 1.0, 3.0)

		video.finishNewFrame()

		pygame.time.wait(33)

if __name__ == "__main__":
	main()
