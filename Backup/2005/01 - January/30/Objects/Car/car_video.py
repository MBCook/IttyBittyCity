from OpenGL.GL import *

def makeDisplayList():
    """This makes a display list containing our car."""

    # First we have to get all the vertex data out of the car_data.py file
    # This uses some magic in the form of the built in function "execfile".

    car_dict = {}

    execfile("car_data.py", car_dict)

    # OK, if that worked, we have everything we need in car_dict
    # So now we run the function in the file

    makeCarData = car_dict['makeCarData']

    (body_data, tire_data, headlight_data,
         brake_data, window_data) = makeCarData()

    giantList = body_data + tire_data + headlight_data + brake_data + window_data

    bodyStarts = 0
    bodyCount = len(body_data) / 10
    tireStarts = len(body_data)
    tireCount = len(tire_data) / 10
    headlightStarts = tireStarts + len(tire_data)
    headlightCount = len(headlight_data) / 10
    brakeStarts = headlightStarts + len(headlight_data)
    brakeCount = len(brake_data) / 10
    windowStarts = brakeStarts + len(brake_data)
    windowCount = len(window_data) / 10

    # Wow! All that works! OK, time to make us a display list.
    # Here's how it will work. We do:
    #
    #   1. Draw the body data
    #   2. Translate and draw the four tires
    #   3. Translate and draw the headlights
    #   4. Translate and draw the brakelights
    #   5. Draw the window data

    carDisplayList = glGenLists(1)

    if carDisplayList == 0:
        return                   # Something went wrong

    # Load up our massive array

    glInterleavedArrays(GL_C4F_N3F_V3F, 0, giantList)

    # Now tell OpenGL what we want out of the array

    glEnableClientState(GL_COLOR_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glEnableClientState(GL_VERTEX_ARRAY)

    # Star the list

    glNewList(carDisplayList, GL_COMPILE)

    # Draw things! Now we do the body

    glDrawArrays(GL_TRIANGLE, bodyStarts, bodyCount)

    # Now we do the wheels

    glPushMatrix()
    glTranslatef(0.75, 1.5, 0.0)
    glDrawArrays(GL_TRIANGLE, wheelStarts, wheelCount)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.75, 6.5, 0.0)
    glDrawArrays(GL_TRIANGLE, wheelStarts, wheelCount)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.25, 1.5, 0.0)
    glDrawArrays(GL_TRIANGLE, wheelStarts, wheelCount)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.25, 6.5, 0.0)
    glDrawArrays(GL_TRIANGLE, wheelStarts, wheelCount)
    glPopMatrix()

    # Now we do the headlights

    glPushMatrix()
    glTranslatef(0.5, 8.5, 2.0)
    glDrawArrays(GL_TRIANGLE, headlightStarts, headlightCount)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.5, 8.5, 2.0)
    glDrawArrays(GL_TRIANGLE, headlightStarts, headlightCount)
    glPopMatrix()

    # Now we do the brakelights

    glPushMatrix()
    glTranslatef(0.875, 0.0, 1.875)
    glDrawArrays(GL_TRIANGLE, headlightStarts, headlightCount)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.125, 0.0, 1.875)
    glDrawArrays(GL_TRIANGLE, headlightStarts, headlightCount)
    glPopMatrix()

    # Now we do the windows

    glDrawArrays(GL_TRIANGLE, windowStarts, windowCount)
    

    # End the list

    glEndList()

    # Return the display list number

    return carDisplayList