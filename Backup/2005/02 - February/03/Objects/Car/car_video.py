from OpenGL.GL import *
from VideoRoutines import *

def makeDisplayList(mode, num = 0):
    """This makes a display list containing our car."""

    # First we have to get all the vertex data out of the car_data.py file
    # This uses some magic in the form of the built in function "execfile".
    # We have to do this because otherwise Python doesn't like the formulas in
    #   the list.

    car_dict = {}

    execfile("car_data.py", car_dict)

    # OK, if that worked, we have everything we need in car_dict
    # So now we run the function in the file

    makeCarData = car_dict['makeCarData']

    (body_data, tire_data, headlight_data,
         brake_data, window_data) = makeCarData()

    # Wow! All that works! OK, time to make us a display list.
    # Here's how it will work. We do:
    #
    #   1. Draw the body data
    #   2. Translate and draw the four tires
    #   3. Translate and draw the headlights
    #   4. Translate and draw the brakelights
    #   5. Draw the window data

    if ((num == 0) or (num == None)):
        # We don't have a display list, get one
        carDisplayList = glGenLists(1)
    else:
        # Use the one we already have
        carDisplayList = num

    if carDisplayList == 0:
        except NameError, "Given bad display list number (0)."

    # Star the list

    glNewList(carDisplayList, GL_COMPILE)

    # Draw the car centered at the origin (with wheels touching XY plane)

    glTranslatef(2.0, 4.25, 0.0)

    # Draw things! Now we do the body

    drawFromArray(body_data, mode)

    # Now we do the wheels

    glPushMatrix()
    glTranslatef(0.75, 1.5, 0.0)
    drawFromArray(tire_data, mode)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.75, 6.5, 0.0)
    drawFromArray(tire_data, mode)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.25, 1.5, 0.0)
    drawFromArray(tire_data, mode)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.25, 6.5, 0.0)
    drawFromArray(tire_data, mode)
    glPopMatrix()

    # Now we do the headlights

    glPushMatrix()
    glTranslatef(0.5, 8.5, 2.0)
    drawFromArray(headlight_data, mode)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.5, 8.5, 2.0)
    drawFromArray(headlight_data, mode)
    glPopMatrix()

    # Now we do the brakelights

    glPushMatrix()
    glTranslatef(0.875, 0.0, 1.875)
    drawFromArray(brake_data, mode)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.125, 0.0, 1.875)
    drawFromArray(brake_data, mode)
    glPopMatrix()

    # Now we do the windows

    drawFromArray(window_data, mode)

    # End the list

    glEndList()

    # Return the display list number

    return carDisplayList