from OpenGL.GL import *

def drawFromArray(array, mode):
    """Draw the triangles in the array."""

    # Yeah, this is kind of ugly. But it should work, and it gives me more controll.
    # And it's not like it's performance sensitive, since this is run at startup
    #   and then a display list is used for actual displaying.

    # 1 draws the points
    # 2 draws wires
    # 3 draws polygons
    # 4 draws normals
    # 5 draws polygons, normals, and wires

    if mode == 5:   # Everything
        drawFromArray(array, 3)
        drawFromArray(array, 2)
        drawFromArray(array, 4)
        return

    vertexCount = len(array) / 30

    for j in range(vertexCount)
        if mode == 3:   # Polygons

            glBegin(GL_TRIANGLES)

            for i in range(3):
                glColor4f(array[j * 30 + i * 10], array[j * 30 + i * 10 + 1],
                            array[j * 30 + i * 10 + 2], array[j * 30 + i * 10 + 3])
                glNormal3f(array[j * 30 + i * 10 + 4], array[j * 30 + i * 10 + 5],
                            array[j * 30 + i * 10 + 6])
                glVertex3f(array[j * 30 + i * 10 + 7], array[j * 30 + i * 10 + 8],
                            array[j * 30 + i * 10 + 9])

            glEnd()

        elif mode == 4: # Normals

            x = 0.0
            nx = 0.0
            y = 0.0
            ny = 0.0
            z = 0.0
            nz = 0.0

            for i in range(3):
                nx += array[j * 30 + i * 10 + 4]
                ny += array[j * 30 + i * 10 + 5]
                nz += array[j * 30 + i * 10 + 6]
                x += array[j * 30 + i * 10 + 7]
                y += array[j * 30 + i * 10 + 8]
                z += array[j * 30 + i * 10 + 9]

            nx = nx / 3.0
            ny = ny / 3.0
            nz = nz / 3.0
            x = x / 3.0
            y = y / 3.0
            z = z / 3.0

            glBegin(GL_LINES):
                glColor4f(0.0, 0.0, 0.0, 1.0)
                glVertex3f(x, y, z)
                glVertex3f(x + nx, y + ny, z + nz)
            glEnd()            
            
        elif mode == 2: # Wireframe
            glBegin(GL_LINES)
            for i in range(3):
                glColor4f(array[j * 30 + i * 10], array[j * 30 + i * 10 + 1],
                            array[j * 30 + i * 10 + 2], array[j * 30 + i * 10 + 3])
                glVertex3f(array[j * 30 + i * 10 + 7], array[j * 30 + i * 10 + 8],
                            array[j * 30 + i * 10 + 9])
                glColor4f(array[j * 30 + (i + 1) * 10], array[j * 30 + (i + 1) * 10 + 1],
                            array[j * 30 + (i + 1) * 10 + 2], array[j * 30 + (i + 1) * 10 + 3])
                glVertex3f(array[j * 30 + (i + 1) * 10 + 7], array[j * 30 + (i + 1) * 10 + 8],
                            array[j * 30 + (i + 1) * 10 + 9])
                
                glColor4f(array[j * 30 + (i + 1) * 10], array[j * 30 + (i + 1) * 10 + 1],
                            array[j * 30 + (i + 1) * 10 + 2], array[j * 30 + (i + 1) * 10 + 3])
                glVertex3f(array[j * 30 + (i + 1) * 10 + 7], array[j * 30 + (i + 1) * 10 + 8],
                            array[j * 30 + (i + 1) * 10 + 9])
                glColor4f(array[j * 30 + (i + 2) * 10], array[j * 30 + (i + 2) * 10 + 1],
                            array[j * 30 + (i + 2) * 10 + 2], array[j * 30 + (i + 2) * 10 + 3])
                glVertex3f(array[j * 30 + (i + 2) * 10 + 7], array[j * 30 + (i + 2) * 10 + 8],
                            array[j * 30 + (i + 2) * 10 + 9])

                glColor4f(array[j * 30 + (i + 2) * 10], array[j * 30 + (i + 2) * 10 + 1],
                            array[j * 30 + (i + 2) * 10 + 2], array[j * 30 + (i + 2) * 10 + 3])
                glVertex3f(array[j * 30 + (i + 2) * 10 + 7], array[j * 30 + (i + 2) * 10 + 8],
                            array[j * 30 + (i + 2) * 10 + 9])
                glColor4f(array[j * 30 + i * 10], array[j * 30 + i * 10 + 1],
                            array[j * 30 + i * 10 + 2], array[j * 30 + i * 10 + 3])
                glVertex3f(array[j * 30 + i * 10 + 7], array[j * 30 + i * 10 + 8],
                            array[j * 30 + i * 10 + 9])
            glEnd()
        elif mode == 1: # Points
            glBegin(GL_POINTS)
            for i in range(3):
                glColor4f(array[j * 30 + i * 10], array[j * 30 + i * 10 + 1],
                            array[j * 30 + i * 10 + 2], array[j * 30 + i * 10 + 3])
                glVertex3f(array[j * 30 + i * 10], array[j * 30 + i * 10],
                            array[j * 30 + i * 10 + 2], array[j * 30 + i * 10 + 3])
            glEnd()
        else:
            return False    # Shouldn't get here

    return True             # Things worked (at least, no errors)

def makeDisplayList(mode):
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
        return 0    # Something went wrong

    # Star the list

    glNewList(carDisplayList, GL_COMPILE)

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