import Preferences
import pygame
import SimulationObject
from OpenGL.GL import *
from OpenGL.GLU import *
from VideoRoutines import *

class Video:
	"""Video handles all the video stuff for us."""

	cameraX = 0.0
	cameraY = 0.0
	cameraZ = 0.0
	cameraUpX = 0.0
	cameraUpY = 0.0
	cameraUpZ = 0.0
	cameraPointX = 0.0
	cameraPointY = 0.0
	cameraPointZ = 0.0
	windowHeight = 0
	windowWidth = 0
	lightX = 0.0
	lightY = 0.0
	lightZ = 0.0

	def __init__(self, prefObject):
		"""Prepare the video class for us."""

		if prefObject == None:
			raise NameError, "No preference object recieved."

		self.Prefs = prefObject

		# Not we load the preferences we need to know

		self.cameraX = self.Prefs.getPref("cameraX")
		self.cameraY = self.Prefs.getPref("cameraY")
		self.cameraZ = self.Prefs.getPref("cameraZ")

		self.cameraUpX = self.Prefs.getPref("cameraUpX")
		self.cameraUpY = self.Prefs.getPref("cameraUpY")
		self.cameraUpZ = self.Prefs.getPref("cameraUpZ")

		self.cameraPointX = self.Prefs.getPref("cameraPointX")
		self.cameraPointY = self.Prefs.getPref("cameraPointY")
		self.cameraPointZ = self.Prefs.getPref("cameraPointZ")

		self.windowWidth = self.Prefs.getPref("windowWidth")
		self.windowHeight = self.Prefs.getPref("windowHeight")

		self.lightX = self.Prefs.getPref("lightX")
		self.lightY = self.Prefs.getPref("lightY")
		self.lightZ = self.Prefs.getPref("lightZ")

		# Prepare the texture cache

		initTextureCache()

	def renderFrame(self):
		"""Render a frame. Uses all the helper functions."""

		self.prepareNewFrame()
		self.setupCamera()
		self.setupLights()
		self.drawScenery()
		self.drawObjects()
		self.drawActors()
		self.drawOverlays()
		self.finishNewFrame()

	def prepareVideo(self):
		"""Set things up (including loading OpenGL)."""

		w = self.Prefs.getPref("windowWidth")
		h = self.Prefs.getPref("windowHeight")

		# Prepare a window for us

		pygame.display.set_mode((w, h), pygame.OPENGL | pygame.DOUBLEBUF)

		# Set up OpenGL stuff

		glMatrixMode(GL_PROJECTION)

		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_SMOOTH)
		glEnable(GL_COLOR_MATERIAL)
		glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
		glEnable(GL_NORMALIZE)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glEnable(GL_POLYGON_SMOOTH)
		glEnable(GL_LINE_SMOOTH)
		glEnable(GL_TEXTURE_2D)
		glEnable(GL_LIGHTING)

		glClearColor(0.0, 0.0, 0.0, 0.0)

		# This is also where we would load textures for the whole application

	def prepareNewFrame(self):
		"""Start a new frame. Clear things, set states, etc."""

		# Clear out the buffer

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	def setupCamera(self):
		"""Put the camera where we want it."""

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45.0, self.Prefs.getPref("windowWidth") / self.Prefs.getPref("windowHeight"),
						0.2, 60.0)

		gluLookAt(self.Prefs.getPref("cameraX"),
				  self.Prefs.getPref("cameraY"),
				  self.Prefs.getPref("cameraZ"),
				  self.Prefs.getPref("cameraPointX"),
				  self.Prefs.getPref("cameraPointY"),
				  self.Prefs.getPref("cameraPointZ"),
				  self.Prefs.getPref("cameraUpX"),
				  self.Prefs.getPref("cameraUpY"),
				  self.Prefs.getPref("cameraUpZ"))

	def setupLights(self):
		"""Put the light(s) where we want 'em."""

		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()

		# Some ambient light for the scene

		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (1.0, 1.0, 1.0, 1.0))

		# Our main light, color and position.
		
		glLightfv(GL_LIGHT1, GL_DIFFUSE, (0.75, 0.75, 0.75, 1.0))
		glLightfv(GL_LIGHT1, GL_POSITION, (self.Prefs.getPref("lightX"),
										   self.Prefs.getPref("lightY"),
										   self.Prefs.getPref("lightZ"),
										   0.0))
		glEnable(GL_LIGHT1)

	def drawScenery(self):
		"""Draw the background stuff (ground, sky, etc.)"""
		pass

	def drawObjects(self):
		"""Draw buildings, mailboxes, and other such objects."""
		pass

	def drawActors(self):
		"""Draw cars, people, animals, and other such things."""
		pass

	def drawOverlays(self):
		"""Draw any overlays that go on top of the image."""
		pass

	def finishNewFrame(self):
		"""Finish up making the new frame."""

		glPopMatrix()

		# Complete all drawing

		glFlush()

		# Swap the buffers

		pygame.display.flip()
