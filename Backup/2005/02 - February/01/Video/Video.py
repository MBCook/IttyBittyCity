from OpenGL.GL import *
from OpenGL.GLU import *

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
    pass

def prepareNewFrame():
    """Start a new frame. Clear things, set states, etc."""
    pass

def setupCamera():
    """Put the camera where we want it."""
    pass

def setupLights():
    """Put the light(s) where we want 'em."""
    pass

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
    pass
