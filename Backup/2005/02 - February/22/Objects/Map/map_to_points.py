def pointListForGrass(x, y):
	"""Generate the point list for grass and the connectios"""

	return []	# No points are made for grass

def pointListForT(x, y, type):
	"""Generate the point list for a T intersection."""

	pointList = []

	if x < 10:
		xString = "0%d" % x
	else:
		xString = "%d" % x

	if x < 11:
		xMString = "0%d" % (x - 1)
	else:
		xMString = "%d" % (x - 1)

	if x < 9:
		xPString = "0%d" % (x + 1)
	else:
		xPString = "%d" % (x + 1)

	if y < 11:
		yMString = "0%d" % (y - 1)
	else:
		yMString = "%d" % (y - 1)

	if y < 9:
		yPString = "0%d" % (y + 1)
	else:
		yPString = "%d" % (y + 1)

	if y < 10:
		yString = "0%d" % y
	else:
		yString = "%d" % y

	if type == 3:		# Down
		tl = ["%s%sTL" % (xString, yString), 0.25, 0.25, [	"%s%sTR" % (xMString, yString)]]
		tr = ["%s%sTR" % (xString, yString), 0.75, 0.25, [	"%s%sTL" % (xString, yString),
															"%s%sCC" % (xString, yString)]]
		bl = ["%s%sBL" % (xString, yString), 0.25, 0.75, [	"%s%sBR" % (xString, yString),
															"%s%sTL" % (xString, yPString)]]
		br = ["%s%sBR" % (xString, yString), 0.75, 0.75, [	"%s%sBL" % (xPString, yString),
															"%s%sCC" % (xString, yString)]]
		cc = ["%s%sCC" % (xString, yString), 0.50, 0.50, [	"%s%sTL" % (xString, yString),
															"%s%sBL" % (xString, yString),
															"%s%sBR" % (xString, yString)]]
	elif type == 4:		# Left
		tl = ["%s%sTL" % (xString, yString), 0.25, 0.25, [	"%s%sTR" % (xMString, yString),
															"%s%sBL" % (xString, yString)]
		tr = ["%s%sTR" % (xString, yString), 0.75, 0.25, [	"%s%sBR" % (xString, yMString)]]
		bl = ["%s%sBL" % (xString, yString), 0.25, 0.75, [	"%s%sTL" % (xString, yPString),
															"%s%sCC" % (xString, yString)]]
		br = ["%s%sBR" % (xString, yString), 0.75, 0.75, [	"%s%sTR" % (xString, yString),
															"%s%sCC" % (xString, yString)]]
		cc = ["%s%sCC" % (xString, yString), 0.50, 0.50, [	"%s%sTL" % (xString, yString),
															"%s%sTR" % (xString, yString),
															"%s%sBL" % (xString, yString)]]	
	elif type == 5:		# Up
		tl = ["%s%sTL" % (xString, yString), 0.25, 0.25, [	"%s%sTR" % (xMString, yString),
															"%s%sCC" % (xString, yString)]]
		tr = ["%s%sTR" % (xString, yString), 0.75, 0.25, [	"%s%sTL" % (xString, yString),
															"%s%sBR" % (xString, yMString)]]
		bl = ["%s%sBL" % (xString, yString), 0.25, 0.75, [	"%s%sBR" % (xString, yString),
															"%s%sTL" % (xString, yPString)]]
		br = ["%s%sBR" % (xString, yString), 0.75, 0.75, [	"%s%sTR" % (xString, yString),
															"%s%sCC" % (xString, yString)]]
		cc = ["%s%sCC" % (xString, yString), 0.50, 0.50, [	"%s%sTL" % (xString, yString),
															"%s%sTR" % (xString, yString),
															"%s%sBL" % (xString, yString),
															"%s%sBR" % (xString, yString)]]
	else: # Type == 6	# Right
		tl = ["%s%sTL" % (xString, yString), 0.25, 0.25, [	"%s%sBL" % (xString, yString),
															"%s%sCC" % (xString, yString)]]
		tr = ["%s%sTR" % (xString, yString), 0.75, 0.25, [	"%s%sBR" % (xString, yMString),
															"%s%sCC" % (xString, yString)]]
		bl = ["%s%sBL" % (xString, yString), 0.25, 0.75, [	"%s%sBR" % (xString, yString),
															"%s%sTL" % (xString, yPString),
		br = ["%s%sBR" % (xString, yString), 0.75, 0.75, [	"%s%sBL" % (xPString, yString),
															"%s%sTR" % (xString, yString)]]
		cc = ["%s%sCC" % (xString, yString), 0.50, 0.50, [	"%s%sTR" % (xString, yString),
															"%s%sBL" % (xString, yString),
															"%s%sBR" % (xString, yString)]]

	pointList = [tr, tr, bl, br, cc]

def pointListForCurve(x, y, type):
	"""Genereate the point list for a curve of the given type."""

	if x < 10:
		xString = "0%d" % x
	else:
		xString = "%d" % x

	if x < 11:
		xMString = "0%d" % (x - 1)
	else:
		xMString = "%d" % (x - 1)

	if x < 9:
		xPString = "0%d" % (x + 1)
	else:
		xPString = "%d" % (x + 1)

	if x < 8:
		xPPString = "0%d" % (x + 2)
	else:
		xPPString = "%d" % (x + 2)

	if y < 11:
		yMString = "0%d" % (y - 1)
	else:
		yMString = "%d" % (y - 1)

	if y < 9:
		yPString = "0%d" % (y + 1)
	else:
		yPString = "%d" % (y + 1)

	if y < 8:
		yPPString = "0%d" % (y + 2)
	else:
		yPPString = "%d" % (y + 2)

	if y < 10:
		yString = "0%d" % y
	else:
		yString = "%d" % y

	innerRadius = 56.0 / 64.0
	outerRadius = 93.0 / 64.0

	slices = 10

	# Dots are numbered as xxyy[IO]z
	# The I means it is the inside trek, the O the outside
	# The z is which particular dot it is (0-9)
	# Note that all paths are marked as being inside the top-left square
	# Except for entrence and exit dots.
	# Curves are generated from star + 10 to end - 10

	if type == 8:			# Bottom right
		centerX = 25.0 / 64.0
		centerY = 25.0 / 64.0
		start = 90.0
		end = 180.0

		enterIn =	["%s%sTL" % (xPString, yString), 0.25, 0.25, ["%s%sI0" % (xString, yString)]]
		enterOut =	["%s%sBL" % (xString, yPString), 0.25, 0.75, ["%s%sO0" % (xString, yString)]]
		exitIn =	["%s%sTL" % (xString, yPString), 0.25, 0.25, ["%s%sTR" % (xMString, yString)]]
		exitOut =	["%s%sTR" % (xString, yString), 0.75, 0.25, ["%s%sBR" % (xString, yMString)]]

		endIn = "%s%sTL" % (xString, yPString)
		endOut = "%s%sTR" % (xString, yString)

	elif type == 9:			# Bottom left
		centerX = 103.0 / 64.0
		centerY = 25.0 / 64.0
		start = 180.0
		end = 270.0

		enterIn =	["%s%sTR" % (xPString, yString), 0.25, 0.75, ["%s%sI0" % (xString, yString)]]
		enterOut =	["%s%sTL" % (xString, yString), 0.25, 0.25, ["%s%sO0" % (xString, yString)]]
		exitIn =	["%s%sTR" % (xString, yString), 0.25, 0.75, ["%s%sBR" % (xString, yMString)]]
		exitOut =	["%s%sBR" % (xPString, yString), 0.75, 0.75, ["%s%sBL" % (xPPString, yPString)]]

		endIn = "%s%sTR" % (xString, yString)
		endOut = "%s%sBR" % (xPString, yString)

	elif type == 10:		# Top left
		centerX = 103.0 / 64.0
		centerY = 103.0 / 64.0
		start = 270.0
		end = 360.0

		enterIn =	["%s%sBR" % (xString, yPString), 0.75, 0.75, ["%s%sI0" % (xString, yString)]]
		enterOut =	["%s%sTR" % (xPString, yString), 0.75, 0.25, ["%s%sO0" % (xString, yString)]]
		exitIn =	["%s%sBR" % (xPString, yString), 0.75, 0.75, ["%s%sBL" % (xPPString, yString)]]
		exitOut =	["%s%sBL" % (xString, yPString), 0.25, 0.75, ["%s%sTL" % (xString, yPPString)]]

		endIn = "%s%sBR" % (xPString, yString)
		endOut = "%s%sBL" % (xString, yPString)

	else: # type == 11:		# Top right
		centerX = 25.0 / 64.0
		centerY = 103.0 / 64.0
		start = 0.0
		end = 90.0

		enterIn =	["%s%sBR" % (xString, yString), 0.75, 0.75, ["%s%sI0" % (xString, yString)]]
		enterOut =	["%s%sBR" % (xPString, yPString), 0.75, 0.75, ["%s%sO0" % (xString, yString)]]
		exitIn =	["%s%sBL" % (xPString, yPString), 0.25, 0.75, ["%s%sTL" % (xPString, yPPString)]]
		exitOut =	["%s%sTL" % (xString, yString), 0.25, 0.25, ["%s%sTR" % (xMString, yString)]]

		endIn = "%s%sBL" % (xPString, yPString)
		endOut = "%s%sTL" % (xString, yString)

	pointList = [enterIn, enterOut, exitIn, exitOut]

	string = "%s%s" % (xString, yString)
	step = (end - 10.0) - (start + 10.0)

	for i in range(10):
		if i < 9:
			temp = ["%sI%d" % (string, i), centerX + cos(radians(start + step * i),
													centerY + sin(radians(start + step * i),
													["%sI%d" % string, i + 1]]
		else:
			temp = ["%sI%d" % (string, i), centerX + cos(radians(start + step * i),
													centerY + sin(radians(start + step * i),
													[endIn]]

		pointList.push(temp)

		if i < 9:
			temp = ["%sO%d" % (string, i), centerX + cos(radians(start + step * (9 - i)),
													centerY + sin(radians(start + step * (9 - i)),
													["%sO%d" % string, i + 1]]
		else:
			temp = ["%sO%d" % (string, i), centerX + cos(radians(start + step * (9 - i)),
													centerY + sin(radians(start + step * (9 - i)),
													[endIn]]

		pointList.push(temp)

	return pointLIst

def pointListForHorizontal(x, y):
	"""Genereate the point list for horizontal and the connections"""

	pointList = []

	if x < 10:
		xString = "0%d" % x
	else:
		xString = "%d" % x

	if x < 11:
		xMString = "0%d" % (x - 1)
	else:
		xMString = "%d" % (x - 1)

	if x < 9:
		xPString = "0%d" % (x + 1)
	else:
		xPString = "%d" % (x + 1)

	if y < 10:
		yString = "0%d" % y
	else:
		yString = "%d" % y

	tl = ["%s%sTL" % (xString, yString), 0.25, 0.25, ["%s%sTR" % (xMString, yString)]]
	tr = ["%s%sTR" % (xString, yString), 0.75, 0.25, ["%s%sTL" % (xString, yString)]]
	bl = ["%s%sBL" % (xString, yString), 0.25, 0.75, ["%s%sBR" % (xString, yString)]]
	br = ["%s%sBR" % (xString, yString), 0.75, 0.75, ["%s%sBL" % (xPString, yString)]]

	pointList = [tr, tr, bl, br]

	return pointList

def pointListForVirticle(x, y):
	"""Genereate the point list for virticle and the connections"""

	pointList = []

	if x < 10:
		xString = "0%d" % x
	else:
		xString = "%d" % x

	if y < 11:
		yMString = "0%d" % (y - 1)
	else:
		yMString = "%d" % (y - 1)

	if y < 9:
		yPString = "0%d" % (y + 1)
	else:
		yPString = "%d" % (y + 1)

	if y < 10:
		yString = "0%d" % y
	else:
		yString = "%d" % y

	tl = ["%s%sTL" % (xString, yString), 0.25, 0.25, ["%s%sBL" % (xString, yString)]]
	tr = ["%s%sTR" % (xString, yString), 0.75, 0.25, ["%s%sBR" % (xString, yMString)]]
	bl = ["%s%sBL" % (xString, yString), 0.25, 0.75, ["%s%sTL" % (xString, yPString)]]
	br = ["%s%sBR" % (xString, yString), 0.75, 0.75, ["%s%sTR" % (xString, yString)]]

	pointList = [tr, tr, bl, br]

	return pointList

def pointListForPlus(x, y):
	"""Genereate the point list for plus and the connections"""

	pointList = []

	if x < 10:
		xString = "0%d" % x
	else:
		xString = "%d" % x

	if x < 11:
		xMString = "0%d" % (x - 1)
	else:
		xMString = "%d" % (x - 1)

	if x < 9:
		xPString = "0%d" % (x + 1)
	else:
		xPString = "%d" % (x + 1)

	if y < 11:
		yMString = "0%d" % (y - 1)
	else:
		yMString = "%d" % (y - 1)

	if y < 9:
		yPString = "0%d" % (y + 1)
	else:
		yPString = "%d" % (y + 1)

	if y < 10:
		yString = "0%d" % y
	else:
		yString = "%d" % y

	tl = ["%s%sTL" % (xString, yString), 0.25, 0.25, [	"%s%sTR" % (xMString, yString),
														"%s%sBL" % (xString, yString),
														"%s%sCC" % (xString, yString)]]
	tr = ["%s%sTR" % (xString, yString), 0.75, 0.25, [	"%s%sTL" % (xString, yString),
														"%s%sBR" % (xString, yMString),
														"%s%sCC" % (xString, yString)]]
	bl = ["%s%sBL" % (xString, yString), 0.25, 0.75, [	"%s%sBR" % (xString, yString),
														"%s%sTL" % (xString, yPString),
														"%s%sCC" % (xString, yString)]]
	br = ["%s%sBR" % (xString, yString), 0.75, 0.75, [	"%s%sBL" % (xPString, yString),
														"%s%sTR" % (xString, yString),
														"%s%sCC" % (xString, yString)]]
	cc = ["%s%sCC" % (xString, yString), 0.50, 0.50, [	"%s%sTL" % (xString, yString),
														"%s%sTR" % (xString, yString),
														"%s%sBL" % (xString, yString),
														"%s%sBR" % (xString, yString)]]

	pointList = [tr, tr, bl, br, cc]

	return pointList
