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
import Simulation
import Map
import test_map
import pickle

from OpenGL.GL import *

def main():
	"""The main program."""

	print ""

	# Initialize Pygame

	print "Starting Pygame..."

	pygame.init()

	# First we set some stuff up.

	print "Initializing stuff..."

	prefs = Preferences.Preferences()
	prefs.loadPreferences()
	video = Video.Video(prefs)
	video.prepareVideo()

	simulationObject = Simulation.Simulation()

	carObject = Car.Car()
	groundObject = Map.Map()

	print "Unpickleing dictionaries..."

	nodeFile = open("Objects/Map/node_list.dat", "r")
	distFile = open("Objects/Map/node_distances.dat", "r")

	nodeDict = pickle.load(nodeFile)
	distDict = pickle.load(distFile)

	nodeFile.close()
	distFile.close()

	print "initializing more stuff..."

	groundObject.loadMapData(test_map.t_d, test_map.t_w, test_map.t_h, nodeDict, distDict)
	groundObject.setupObjects()

	simulationObject.setMap(groundObject)
	simulationObject.addObject(carObject)

	print "Preparing stuff for the car..."

	carObject.setXYPosition(2.25, 0.25)
	carObject.setCurrentNode("0200TL")
	carObject.setVelocity(2.0)
	carObject.getNextTarget()

	# Now we do things

	print "Preparing lists for drawing paths..."

	(points, lines) = VideoRoutines.drawPathsPrep(nodeDict, distDict)

	print "Starting main loop..."

	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		simulationObject.update(33.0 / 1000.0)

		video.prepareNewFrame()
		video.setupCamera()
		video.setupLights()

		# Drawing happens here

		glLoadIdentity()

#		groundObject.draw()
#		carObject.draw()

		simulationObject.draw()

		glLoadIdentity()

#		VideoRoutines.drawPaths(points, lines, 20.0, 1.0, 3.0)
		VideoRoutines.drawSpecialPath(carObject.getPath(), nodeDict, 20.0, 1.0, 3.0)

		video.finishNewFrame()

		pygame.time.wait(33)

	print "Exiting..."
	print ""

if __name__ == "__main__":
	main()
