import math

# This file contains the vertex data for the little car in various arrays

def tcx(num):
	"""Make a texture coordinate."""

	return num / 14.0

def tcy(num):
	"""Make a texture coordinate."""

	return num / 14.0

def makeCarData():
	"""Return the car data."""

	radTwoOverTwo = math.sqrt(2.0) / 2.0	# Used as part of normal to 45 degree angle

	sideHigh = 0.5 / math.sqrt(0.5 * 0.5 + 2 * 2)	# Used in the normals on the windows
	sideLong = 2 / math.sqrt(0.5 * 0.5 + 2 * 2)

	carColorRed = 1.0
	carColorGreen = 1.0
	carColorBlue = 1.0
	carColorAlpha = 1.0

	carTireRed = 0.0
	carTireGreen = 0.0
	carTireBlue = 0.0
	carTireAlpha = 1.0

	body_data = [	# This is interlieved array of triangles used to specify the car body.
					# The data is in GL_T2F_C4F_N3F_V3F format
					# Car's rear drivers side corner is at origin, facing 0,1,0

		# The two hood triangles first

		tcx(4.0), tcy(2.0),											# Texture
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,	# Color
		0.0, 0.0, 1.0,												# Normal
		0.0, 8.5, 3.0,												# Vertex
		tcx(4.0), tcy(4.0),											# Texture
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,	# Color
		0.0, 0.0, 1.0,												# Normal
		0.0, 6.5, 3.0,												# Vertex
		tcx(8.0), tcy(2.0),											# Texture
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,	# ...
		0.0, 0.0, 1.0,
		4.0, 8.5, 3.0,

		tcx(8.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		4.0, 8.5, 3.0,
		tcx(4.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		0.0, 6.5, 3.0,
		tcx(8.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		4.0, 6.5, 3.0,

		# Now the windshield (not the glass)

		tcx(4.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, radTwoOverTwo , radTwoOverTwo,
		0.0, 6.5, 3.0,
		tcx(4.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, radTwoOverTwo , radTwoOverTwo,
		0.5, 4.5, 5.0,
		tcx(8.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, radTwoOverTwo , radTwoOverTwo,
		4.0, 6.5, 3.0,

		tcx(8.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, radTwoOverTwo , radTwoOverTwo,
		4.0, 6.5, 3.0,
		tcx(4.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, radTwoOverTwo , radTwoOverTwo,
		0.5, 4.5, 5.0,
		tcx(8.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, radTwoOverTwo , radTwoOverTwo,
		3.5, 4.5, 5.0,

		# Now the roof (this is REALLY boring, typing these in)

		tcx(4.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		0.5, 4.5, 5.0,
		tcx(4.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		0.5, 0.5, 5.0,
		tcx(8.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		3.5, 4.5, 5.0,

		tcx(8.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		3.5, 4.5, 5.0,
		tcx(4.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		0.5, 0.5, 5.0,
		tcx(8.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 0.0, 1.0,
		3.5, 0.5, 5.0,

		# Now the rear window panel (again, not the actual window)

		tcx(4.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -sideLong, sideHigh,
		0.5, 0.5, 5.0,
		tcx(4.0), tcy(12.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -sideLong, sideHigh,
		0.0, 0.0, 3.0,
		tcx(8.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -sideLong, sideHigh,
		3.5, 0.5, 5.0,

		tcx(8.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -sideLong, sideHigh,
		3.5, 0.5, 5.0,
		tcx(4.0), tcy(12.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -sideLong, sideHigh,
		0.0, 0.0, 3.0,
		tcx(8.0), tcy(12.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -sideLong, sideHigh,
		4.0, 0.0, 3.0,

		# OK, the car's left side window body pannels, front to back

		tcx(2.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.0, 6.5, 3.0,
		tcx(2.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.0, 4.5, 3.0,
		tcx(4.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.5, 4.5, 5.0,

		tcx(4.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.5, 4.5, 5.0,
		tcx(2.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.0, 4.5, 3.0,
		tcx(4.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.5, 0.5, 5.0,

		tcx(2.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.0, 4.5, 3.0,
		tcx(2.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.0, 0.5, 3.0,
		tcx(4.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.5, 0.5, 5.0,

		tcx(4.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.5, 0.5, 5.0,
		tcx(2.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.0, 0.5, 3.0,
		tcx(2.0), tcy(10.5),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-sideLong, 0.0, sideHigh,
		0.0, 0.0, 3.0,

		# Car's right side, back to front

		tcx(8.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		3.5, 0.5, 5.0,
		tcx(10.0), tcy(10.5),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		4.0, 0.0, 3.0,
		tcx(10.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		4.0, 0.5, 3.0,

		tcx(8.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		3.5, 0.5, 5.0,
		tcx(10.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		4.0, 0.5, 3.0,
		tcx(10.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		4.0, 4.5, 3.0,

		tcx(8.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		3.5, 0.5, 5.0,
		tcx(10.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		4.0, 4.5, 3.0,
		tcx(8.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		3.5, 4.5, 5.0,

		tcx(8.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		3.5, 4.5, 5.0,
		tcx(10.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		4.0, 4.5, 3.0,
		tcx(10.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		sideLong, 0.0, sideHigh,
		4.0, 6.5, 3.0,

		# Car's front bumper

		tcx(8.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 1.0, 0.0,
		4.0, 8.5, 3.0,
		tcx(8.0), tcy(0.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 1.0, 0.0,
		4.0, 8.5, 1.0,
		tcx(4.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 1.0, 0.0,
		0.0, 8.5, 3.0,

		tcx(8.0), tcy(0.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 1.0, 0.0,
		4.0, 8.5, 1.0,
		tcx(4.0), tcy(0.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 1.0, 0.0,
		0.0, 8.5, 1.0,
		tcx(4.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, 1.0, 0.0,
		0.0, 8.5, 3.0,

		# Car's back bumper

		tcx(4.0), tcy(12.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -1.0, 0.0,
		0.0, 0.0, 3.0,
		tcx(4.0), tcy(14.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -1.0, 0.0,
		0.0, 0.0, 1.0,
		tcx(8.0), tcy(12.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -1.0, 0.0,
		4.0, 0.0, 3.0,

		tcx(4.0), tcy(14.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -1.0, 0.0,
		0.0, 0.0, 1.0,
		tcx(8.0), tcy(14.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -1.0, 0.0,
		4.0, 0.0, 1.0,
		tcx(8.0), tcy(12.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		0.0, -1.0, 0.0,
		4.0, 0.0, 3.0,

		# Time for the left side body pannels (front to back again)

		tcx(2.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 8.5, 3.0,
		tcx(0.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 8.5, 1.0,
		tcx(2.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 6.5, 3.0,

		tcx(0.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 8.5, 1.0,
		tcx(0.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 6.5, 1.0,
		tcx(2.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 6.5, 3.0,

		tcx(2.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 6.5, 3.0,
		tcx(0.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 6.5, 1.0,
		tcx(2.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 4.5, 3.0,

		tcx(0.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 6.5, 1.0,
		tcx(0.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 4.5, 1.0,
		tcx(2.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 4.5, 3.0,

		tcx(2.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 4.5, 3.0,
		tcx(0.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 4.5, 1.0,
		tcx(2.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.5, 3.0,

		tcx(0.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 4.5, 1.0,
		tcx(0.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.5, 1.0,
		tcx(2.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.5, 3.0,

		tcx(2.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.5, 3.0,
		tcx(0.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.5, 1.0,
		tcx(2.0), tcy(10.5),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.0, 3.0,

		tcx(0.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.5, 1.0,
		tcx(0.0), tcy(10.5),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.0, 1.0,
		tcx(2.0), tcy(10.5),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		-1.0, 0.0, 0.0,
		0.0, 0.0, 3.0,

		# Now the right side of the car, from back to front

		tcx(10.0), tcy(10.5),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.0, 3.0,
		tcx(12.0), tcy(10.5),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.0, 1.0,
		tcx(12.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.5, 1.0,

		tcx(10.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.5, 3.0,
		tcx(10.0), tcy(10.5),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.0, 3.0,
		tcx(12.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.5, 1.0,

		tcx(10.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.5, 3.0,
		tcx(12.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.5, 1.0,
		tcx(12.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 4.5, 1.0,

		tcx(10.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 4.5, 3.0,
		tcx(10.0), tcy(10.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 0.5, 3.0,
		tcx(12.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 4.5, 1.0,

		tcx(10.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 4.5, 3.0,
		tcx(12.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 4.5, 1.0,
		tcx(12.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 6.5, 1.0,

		tcx(10.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 6.5, 3.0,
		tcx(10.0), tcy(6.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 4.5, 3.0,
		tcx(12.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 6.5, 1.0,

		tcx(10.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 6.5, 3.0,
		tcx(12.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 6.5, 1.0,
		tcx(12.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 8.5, 1.0,

		tcx(10.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 8.5, 3.0,
		tcx(10.0), tcy(4.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 6.5, 3.0,
		tcx(12.0), tcy(2.0),
		carColorRed, carColorGreen, carColorBlue, carColorAlpha,
		1.0, 0.0, 0.0,
		4.0, 8.5, 1.0]

		# That's all of the car body

	tire_data = [	# Draws the tire, centered at the origin, one unit Z+, bottom half only
					# Tire is square (for now?), and made of triangles, aligned w/ car
					# In GL_C4F_N3F_V3F

		# TO_DO: Update to use GLU routines for partial discs and cylinders

		# The tires all use the bottom right corner of the texture so they are colored right

		# Tire's left side

		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		-1.0, 0.0, 0.0,
		-0.25, 1.0, 1.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		-1.0, 0.0, 0.0,
		-0.25, 1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		-1.0, 0.0, 0.0,
		-0.25, -1.0, 1.0,

		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		-1.0, 0.0, 0.0,
		-0.25, 1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		-1.0, 0.0, 0.0,
		-0.25, -1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		-1.0, 0.0, 0.0,
		-0.25, -1.0, 1.0,

		# Tire's right side

		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, -1.0, 1.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, -1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, 1.0, 1.0,

		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, -1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, 1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, 1.0, 1.0,

		# Tire's front side

		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		0.0, 1.0, 0.0,
		0.25, 1.0, 1.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, 1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		-0.25, 1.0, 1.0,

		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, 1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		-0.25, 1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		-0.25, 1.0, 1.0,

		# Tire's back side

		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		-1.0, 0.0, 0.0,
		-0.25, -1.0, 1.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		-0.25, -1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, -1.0, 1.0,

		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		-0.25, -1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, -1.0, 0.0,
		tcx(14.0), tcy(14.0),
		carTireRed, carTireGreen, carTireBlue, carTireAlpha,
		1.0, 0.0, 0.0,
		0.25, -1.0, 1.0]

		# That's all for the tire

	return (body_data, tire_data)