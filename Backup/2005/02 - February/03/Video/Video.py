import Preferences
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Video():
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

    def __init__(prefObject):
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

    def renderFrame():
        """Render a frame. Uses all the helper functions."""

        prepareNewFrame()
        setupCamera()
        setupLights()
        drawScenery()
        drawObjects()
        drawActors()
        drawOverlays()
        finishNewFrame()

    def prepareVideo():
        """Set things up (including loading OpenGL)."""

        # Prepare a window for us

        pygame.display.set_mode((640, 480), pygame.OPENGL | pygame.DOUBLEBUF)

        # Set up OpenGL stuff

        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_NORMALIZE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_POLYGON_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_LIGHTING)

        # This is also where we would load textures

    def prepareNewFrame():
        """Start a new frame. Clear things, set states, etc."""

        # Clear out the buffer

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def setupCamera():
        """Put the camera where we want it."""

        gluLookAt(self.Prefs.getPref("cameraX"),
                  self.Prefs.getPref("cameraY"),
                  self.Prefs.getPref("cameraZ"),
                  self.Prefs.getPref("cameraPointX"),
                  self.Prefs.getPref("cameraPointY"),
                  self.Prefs.getPref("cameraPointZ"),
                  self.Prefs.getPref("cameraUpX"),
                  self.Prefs.getPref("cameraUpY"),
                  self.Prefs.getPref("cameraUpZ"))

    def setupLights():
        """Put the light(s) where we want 'em."""

        # Some ambient light for the scene

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (1.0, 1.0, 1.0, 1.0))

        # Our main light, color and position.
        
        glLightfv(GL_LIGHT1, GL_DIFFUSE, (0.75, 0.75, 0.75, 1.0))
        glLightfv(GL_LIGHT1, GL_POSITION, (self.Prefs.getPref("lightX"),
                                           self.Prefs.getPref("lightY"),
                                           self.Prefs.getPref("lightZ"),
                                           0.0))
        glEnable(GL_LIGHT1)

    def drawScenery():
        """Draw the background stuff (ground, sky, etc.)"""
        pass

    def drawObjects():
        """Draw buildings, mailboxes, and other such objects."""
        pass

    def drawActors():
        """Draw cars, people, animals, and other such things."""
        pass

    def drawOverlays():
        """Draw any overlays that go on top of the image."""
        pass

    def finishNewFrame():
        """Finish up making the new frame."""

        # Complete all drawing

        glFlush()

        # Swap the buffers

        pygame.display.flip()
