from OpenGL.GL import *

def drawFromArray(array, textured):
	"""Draw the triangles in the array. GL_T2F_C4F_N3F_V3F"""

	if textured:
		npt = 36				# Number of things per traingle
	else:
		npt = 30

	vC = len(array) / npt	# Veretex count
	npv = npt / 3			# Number of things per vertex

	glBegin(GL_TRIANGLES)

	if textured:
		for j in range(vC):
			for i in range(3):

				cV = j * npt + i * npv

				glTexCoord2f(array[cV], array[cV + 1])
				glColor4f(array[cV + 2], array[cV + 3],	array[cV + 4], array[cV + 5])
				glNormal3f(array[cV + 6], array[cV + 7], array[cV + 8])
				glVertex3f(array[cV + 9], array[cV + 10], array[cV + 11])

	else:
		for j in range(vC):
			for i in range(3):

				cV = j * npt + i * npv

				glColor4f(array[cV], array[cV + 1],	array[cV + 2], array[cV + 3])
				glNormal3f(array[cV + 4], array[cV + 5], array[cV + 6])
				glVertex3f(array[cV + 7], array[cV + 8], array[cV + 9])

	glEnd()
