import math

# This file contains the vertex data for the little car in various arrays

def makeCarData():

    radTwoOverTwo = math.sqrt(2.0) / 2.0    # Used as part of normal to 45 degree angle

    sideHigh = 0.5 / math.sqrt(0.5 * 0.5 + 2 * 2)   # Used in the normals on the windows
    sideLong = 2 / math.sqrt(0.5 * 0.5 + 2 * 2)

    octogonLarge = 0.75 * math.cos(math.radians(22.5))
    octogonSmall = 0.75 * math.sin(math.radians(22.5))

    carColorRed = 0.75
    carColorGreen = 0.0
    carColorBlue = 0.0
    carColorAlpha = 1.0

    carTireRed = 0.2
    carTireGreen = 0.2
    carTireBlue = 0.2
    carTireAlpha = 1.0

    headlightRed = 0.9
    headlightGreen = 0.9
    headlightBlue = 0.9
    headlightAlpha = 1.0

    brakeRed = 0.9
    brakeGreen = 0.0
    brakeBlue = 0.0
    brakeAlpha = 1.0

    reverseRed = 0.9
    reverseGreen = 0.9
    reverseBlue = 0.9
    reverseAlpha = 1.0

    windshieldLength = math.sqrt(2.0 * 2.0 + 2.0 * 2.0)
    windshieldDiff = math.sin(math.radians(45.0)) * windshieldLength * 0.05

    windowLength = math.sqrt(0.5 * 0.5 + 2.0 * 2.0)
    windowTall = math.sin(2.0 / windowLength) * windowLength * 0.05
    windowBase = math.sin(0.5 / windowLength) * windowLength * 0.05

    windowRed = 0.7
    windowGreen = 0.7
    windowBlue = 0.7
    windowAlpha = 1.0

    body_data = [   # This is interlieved array of triangles used to specify the car body.
                    # The data is in GL_C4F_N3F_V3F format
                    # Car's rear drivers side corner is at origin, facing 0,1,0

        # The two hood triangles first

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,    # Color
        0.0, 0.0, 1.0,                                              # Normal
        0.0, 8.5, 3.0,                                              # Vertex
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,    # Color
        0.0, 0.0, 1.0,                                              # Normal
        0.0, 6.5, 3.0,                                              # Vertex
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,    # ...
        0.0, 0.0, 1.0,
        4.0, 8.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        4.0, 8.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        0.0, 6.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        4.0, 6.5, 3.0,

        # Now the windshield (not the glass)

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, radTwoOverTwo , radTwoOverTwo,
        0.0, 8.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, radTwoOverTwo , radTwoOverTwo,
        0.5, 4.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, radTwoOverTwo , radTwoOverTwo,
        4.0, 6.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, radTwoOverTwo , radTwoOverTwo,
        4.0, 6.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, radTwoOverTwo , radTwoOverTwo,
        0.5, 4.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, radTwoOverTwo , radTwoOverTwo,
        3.5, 4.5, 5.0,

        # Now the roof (this is REALLY boring, typing these in)

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        0.5, 4.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        0.5, 0.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        3.5, 4.5, 5.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        3.5, 4.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        0.5, 0.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 0.0, 1.0,
        3.5, 0.5, 5.0,

        # Now the rear window panel (again, not the actual window)

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -sideLong, sideHigh,
        0.5, 0.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -sideLong, sideHigh,
        0.0, 0.0, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -sideLong, sideHigh,
        3.5, 0.5, 5.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -sideLong, sideHigh,
        3.5, 0.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -sideLong, sideHigh,
        0.0, 0.0, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -sideLong, sideHigh,
        4.0, 0.0, 3.0,

        # OK, the car's left side window body pannels, front to back

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.0, 6.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.5, 4.5, 5.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.5, 4.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.5, 0.5, 5.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.0, 0.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.5, 0.5, 5.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.5, 0.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.0, 0.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -sideLong, 0.0, sideHigh,
        0.0, 0.0, 3.0,

        # Car's right side, back to front

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        3.5, 0.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        4.0, 0.0, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        4.0, 0.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        3.5, 0.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        4.0, 0.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        4.0, 4.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        3.5, 0.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        4.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        3.5, 4.5, 5.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        3.5, 4.5, 5.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        4.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        sideLong, 0.0, sideHigh,
        4.0, 6.5, 3.0,

        # Car's front bumper

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 1.0, 0.0,
        4.0, 8.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 1.0, 0.0,
        4.0, 8.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 1.0, 0.0,
        0.0, 8.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 1.0, 0.0,
        4.0, 8.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 1.0, 0.0,
        0.0, 8.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, 1.0, 0.0,
        0.0, 8.5, 3.0,

        # Car's back bumper

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -1.0, 0.0,
        0.0, 0.0, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -1.0, 0.0,
        0.0, 0.0, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -1.0, 0.0,
        4.0, 0.0, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -1.0, 0.0,
        0.0, 0.0, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -1.0, 0.0,
        4.0, 0.0, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        0.0, -1.0, 0.0,
        4.0, 0.0, 3.0,

        # Time for the left side body pannels

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 8.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 8.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 6.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 8.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 6.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 6.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 6.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 6.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 4.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 6.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 4.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 4.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 4.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 4.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.5, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.0, 3.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.0, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        -1.0, 0.0, 0.0,
        0.0, 0.0, 3.0,

        # Now the right side of the car, from back to front

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.0, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.0, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.5, 1.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.0, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.5, 1.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 4.5, 1.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 0.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 4.5, 1.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 4.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 6.5, 1.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 6.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 4.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 6.5, 1.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 6.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 6.5, 1.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 8.5, 1.0,

        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 8.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 6.5, 3.0,
        carColorRed, carColorGreen, carColorBlue, carColorAlpha,
        1.0, 0.0, 0.0,
        4.0, 8.5, 1.0]

        # That's all of the car body

    tire_data = [   # Draws the tire, centered at the origin, one unit Z+, bottom half only
                    # Tire is square (for now?), and made of triangles, aligned w/ car
                    # In GL_C4F_N3F_V3F

        # TO_DO: Update to use GLU routines for partial discs and cylinders

        # Tire's left side

        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        -1.0, 0.0, 0.0,
        -0.25, 1.0, 1.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        -1.0, 0.0, 0.0,
        -0.25, 1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        -1.0, 0.0, 0.0,
        -0.25, -1.0, 1.0,

        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        -1.0, 0.0, 0.0,
        -0.25, 1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        -1.0, 0.0, 0.0,
        -0.25, -1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        -1.0, 0.0, 0.0,
        -0.25, -1.0, 1.0,

        # Tire's right side

        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, -1.0, 1.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, -1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, 1.0, 1.0,

        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, -1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, 1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, 1.0, 1.0,

        # Tire's front side

        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        0.0, 1.0, 0.0,
        0.25, 1.0, 1.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, 1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        -0.25, 1.0, 1.0,

        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, 1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        -0.25, 1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        -0.25, 1.0, 1.0,

        # Tire's back side

        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        -1.0, 0.0, 0.0,
        -0.25, -1.0, 1.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        -0.25, -1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, -1.0, 1.0,

        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        -0.25, -1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, -1.0, 0.0,
        carTireRed, carTireGreen, carTireBlue, carTireAlpha,
        1.0, 0.0, 0.0,
        0.25, -1.0, 1.0]

        # That's all for the tire

    headlight_data = [  # A single headlight, centered about the origin, facing Y+
                        # GL_C4F_N3F_V3F

        # TO_DO: Update to use GLU routines for discs

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        -octogonSmall, 0.0, 0.375,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        octogonSmall, 0.0, 0.375,

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        octogonSmall, 0.0, 0.375,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.375, 0.0, octogonSmall,

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.375, 0.0, octogonSmall,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.375, 0.0, -octogonSmall,

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.375, 0.0, -octogonSmall,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.375, 0.0, octogonSmall,

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.375, 0.0, octogonSmall,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        octogonSmall, 0.0, -0.375,

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        octogonSmall, 0.0, -0.375,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        -octogonSmall, 0.0, -0.375,

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        -octogonSmall, 0.0, -0.375,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        -0.375, 0.0, -octogonSmall,

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        -0.375, 0.0, -octogonSmall,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        -0.375, 0.0, octogonSmall,

        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        -0.375, 0.0, octogonSmall,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        0.0, 0.0, 0.0,
        headlightRed, headlightGreen, headlightBlue, headlightAlpha,
        0.0, 1.0, 0.0,
        -octogonSmall, 0.0, 0.375]

        # End of the headlight

    brake_data = [  # Centered at origin, faces -Y, GL_C4F_N3F_V3F

        # Outside light (brake)

        brakeRed, brakeGreen, brakeBlue, brakeAlpha,
        0.0, -1.0, 0.0,
        -0.875, 0.0, 0.375,
        brakeRed, brakeGreen, brakeBlue, brakeAlpha,
        0.0, -1.0, 0.0,
        -0.875, 0.0, -0.375,
        brakeRed, brakeGreen, brakeBlue, brakeAlpha,
        0.0, -1.0, 0.0,
        0.875, 0.0, 0.325,

        brakeRed, brakeGreen, brakeBlue, brakeAlpha,
        0.0, -1.0, 0.0,
        -0.875, 0.0, -0.375,
        brakeRed, brakeGreen, brakeBlue, brakeAlpha,
        0.0, -1.0, 0.0,
        0.875, 0.0, -0.375,
        brakeRed, brakeGreen, brakeBlue, brakeAlpha,
        0.0, -1.0, 0.0,
        0.875, 0.0, 0.375,

        # Inside light (reverse)

        reverseRed, reverseGreen, reverseBlue, reverseAlpha,
        0.0, -1.0, 0.0,
        -0.1875, 0.0, 0.125,
        reverseRed, reverseGreen, reverseBlue, reverseAlpha,
        0.0, -1.0, 0.0,
        -0.1875, 0.0, -0.125,
        reverseRed, reverseGreen, reverseBlue, reverseAlpha,
        0.0, -1.0, 0.0,
        0.1875, 0.0, 0.125,

        reverseRed, reverseGreen, reverseBlue, reverseAlpha,
        0.0, -1.0, 0.0,
        -0.1875, 0.0, -0.125,
        reverseRed, reverseGreen, reverseBlue, reverseAlpha,
        0.0, -1.0, 0.0,
        0.1875, 0.0, -0.125,
        reverseRed, reverseGreen, reverseBlue, reverseAlpha,
        0.0, -1.0, 0.0,
        0.1875, 0.0, 0.125]

        # That's it for the lights

    window_data = [ # Now we do all the windows. I hate trig. GL_C4F_N3F_V3F
                    # Windows are 5% in from the edge (hopefully)

        # First we do the windshield

        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, radTwoOverTwo, radTwoOverTwo,
        3.8, 6.5 - windshieldDiff, 3.0 + windshieldDiff,
        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, radTwoOverTwo, radTwoOverTwo,
        0.2, 6.5 - windshieldDiff, 3.0 + windshieldDiff,
        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, radTwoOverTwo, radTwoOverTwo,
        0.65, 4.5 + windshieldDiff, 5.0 - windshieldDiff,

        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, radTwoOverTwo, radTwoOverTwo,
        3.35, 4.5 + windshieldDiff, 5.0 - windshieldDiff,
        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, radTwoOverTwo, radTwoOverTwo,
        3.8, 6.5 - windshieldDiff, 3.0 + windshieldDiff,
        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, radTwoOverTwo, radTwoOverTwo,
        0.65, 4.5 + windshieldDiff, 5.0 - windshieldDiff,

        # Now the rear window

        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, -sideLong, sideHigh,
        0.65, 0.5 - windowBase, 5.0 - windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, -sideLong, sideHigh,
        0.2, windowBase, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, -sideLong, sideHigh,
        3.35, 0.5 - windowBase, 5.0 - windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, -sideLong, sideHigh,
        0.2, windowBase, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, -sideLong, sideHigh,
        3.8, windowBase, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        0.0, -sideLong, sideHigh,
        3.35, 0.5 - windowBase, 5.0 - windowTall,

        # Now the left side windows, front to back

        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        windowBase, 6.4, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        windowBase, 4.6, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        0.5 - windowBase, 4.6, 5.0 - windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        0.5 - windowBase, 4.4, 5.0 - windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        windowBase, 4.4, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        0.5 - windowBase, 2.6, 5.0 - windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        windowBase, 4.4, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        windowBase, 2.6, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        0.5 - windowBase, 2.6, 5.0 - windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        0.5 - windowBase, 2.4, 5.0 - windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        windowBase, 2.4, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        0.5 - windowBase, 0.6, 5.0 - windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        windowBase, 2.4, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        windowBase, 0.1, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        -sideLong, 0.0, sideHigh,
        0.5 - windowBase, 0.6, 5.0 - windowTall,

        # Now the windows on the right side, back to front

        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        3.5 + windowBase, 0.6, 5.0 - windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        4.0 - windowBase, 0.1, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        4.0 - windowBase, 2.4, 3.0 + windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        3.5 + windowBase, 0.6, 5.0 - windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        4.0 - windowBase, 2.4, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        3.5 + windowBase, 2.4, 5.0 - windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        3.5 + windowBase, 2.6, 5.0 - windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        4.0 - windowBase, 2.6, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        4.0 - windowBase, 4.4, 3.0 + windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        3.5 + windowBase, 2.6, 5.0 - windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        4.0 - windowBase, 4.4, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        3.5 + windowBase, 4.4, 5.0 - windowTall,

        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        3.5 + windowBase, 4.6, 5.0 - windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        4.0 - windowBase, 4.6, 3.0 + windowTall,
        windowRed, windowGreen, windowBlue, windowAlpha,
        sideLong, 0.0, sideHigh,
        4.0 - windowBase, 6.4, 3.0 + windowTall]

        # That's it for the windows

        # In fact, that should be it for the whole car.
        # Let's hope it works right!
        # Now just return all that data we worked out

    return (body_data, tire_data, headlight_data,
                brake_data, window_data)