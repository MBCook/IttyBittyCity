import pickle
import test_map
from math import *

############################################
#
#	For this to work, MAP CAN'T INCLUDE ROAD
#
############################################

def main():
	"""Make the necessary files."""

	global theMap, width, height

	print "Starting to do everything..."
	print "Loading the map..."

	theMap = test_map.t_d
	width = test_map.t_w
	height = test_map.t_h

	print "Starting to process..."
	print ""

	nodeDict, distanceDict = getNodesAndDistances()

	print ""
	print "Got the node and distance dictionaries..."
	print "Opening files..."

	nodes = open("node_list.dat", "w")
	distances = open("node_distances.dat", "w")

	print "Pickleing the node dictionary..."

	pickle.dump(nodeDict, nodes)

	print "Pickeling the distance dictionary..."

	pickle.dump(distanceDict, distances)
	
	print "Closing files..."

	nodes.close()
	distances.close()

	print "Done!"

def getSquare(x, y):
	"""Get the square at x, y."""

	global theMap, width, height

	return theMap[x + y * width]

def getNodesAndDistances():
	"""Get the node list for the map given."""

	global width, height

	# First we generate the list

	print "\tGetting node list..."
	
	nodeDict = {}

	for y in range(height):
		for x in range(width):
			theType = getSquare(x, y)

			print "\t\tGetting list for node (%d, %d) of type %d..." % (x, y, theType)

			tempList = getNodeList(x, y, theType)

			if tempList == []:
				print "\t\t\tNo nodes here."
			else:
				for i in range(len(tempList)):
					node = tempList[i]
					nodeName = node[0]
					nodeDict[nodeName] = node[1:]	# Everything but the first element
					print "\t\t\tAdded node '%s'..." % nodeName

	print "\tDone getting node list (%d nodes)..." % (len(nodeDict.keys()))
	print ""

	# Now that we've got that, we get a list of pairs

	pairList = getPairList(nodeDict)

	# Now we calculate the distance between every pair of nodes that connect

	print ""
	print "\tCreateing dictionary of distances between connected nodes..."

	distanceDict = {}

	for tuple in pairList:
		(nodeA, nodeB) = tuple
		print "\t\tCalculating distance between '%s' and '%s'..." % (nodeA, nodeB)
		distance = distanceBetween(nodeA, nodeB, nodeDict)
		pairName = "%s%s" % (nodeA, nodeB)
		distanceDict[pairName] = distance
		print "\t\t\tDistace was %f." % (distance)

	print "\tDone creating dictionary of node differences (%d pairs)." % (len(distanceDict.keys()))

	return nodeDict, distanceDict

def getPairList(nodeDict):
	"""Make a list of all the pairs of nodes that appear for distance caluclations."""

	pairList = []

	print "\tGetting list of all node pairs..."

	for key in nodeDict.keys():
		print "\t\tLooking at node named '%s'..." % key
		theNode = nodeDict[key]
		connectionsList = theNode[2]
		if (connectionsList == None) or (connectionsList == []):
			# No connections, do nothing
			print "\t\t\tNode has no connections."
			pass
		else:
			for connection in connectionsList:
				if (key < connection):
					theTuple = (key, connection)
				else:
					theTuple = (connection, key)
				if pairList.count(theTuple) == 0:
					print "\t\t\tConection between '%s' and '%s'." % theTuple
					pairList.append(theTuple)
				else:
					print "\t\t\tConection between '%s' and '%s' skipped. Dupe." % theTuple

	print "\tGot list of all node pairs (%d of 'em), sorting it..." % (len(pairList))

	pairList.sort()

	print "\tNode pair list sorted."

	return pairList

def getNodeList(x, y, type):
	"""Get the node list for the given type."""
	
	if type == 0:
		return pointListForGrass(x, y)
	elif type == 1:
		return pointListForHorizontal(x, y)
	elif type == 2:
		return pointListForVirticle(x, y)
	elif type == 3:
		return pointListForT(x, y, type)
	elif type == 4:
		return pointListForT(x, y, type)
	elif type == 5:
		return pointListForT(x, y, type)
	elif type == 6:
		return pointListForT(x, y, type)
	elif type == 7:
		return pointListForPlus(x, y)
	elif type == 8:
		return pointListForCurve(x, y, type)
	elif type == 9:
		return pointListForCurve(x, y, type)
	elif type == 10:
		return pointListForCurve(x, y, type)
	elif type == 11:
		return pointListForCurve(x, y, type)
	else:
		return []

def distanceBetween(nodeOneName, nodeTwoName, nodeDatabase):
	"""Get the distance between two nodes."""

	nodeOnePair = getCoords(nodeOneName, nodeDatabase)
	nodeTwoPair = getCoords(nodeTwoName, nodeDatabase)

	if (nodeOnePair == None) or (nodeTwoPair == None):
		raise NameError, "Unknown node requested, either %s or %s." % (nodeOneName, nodeTwoName)

	(x1, y1) = nodeOnePair
	(x2, y2) = nodeTwoPair

	xPair = pow(x1 - x2, 2)
	yPair = pow(y1 - y2, 2)

	dist = sqrt(xPair + yPair)

	return dist

def getCoords(nodeName, nodeDatabase):
	"""Get the XY position on the map of the node."""

	theNode = nodeDatabase[nodeName]

	if theNode == None:
		return None

	xTen = int(nodeName[0])
	xOne = int(nodeName[1])
	yTen = int(nodeName[2])
	yOne = int(nodeName[3])

	x = xTen * 10 + xOne
	y = yTen * 10 + yOne

	x = float(x) + theNode[0]
	y = float(y) + theNode[1]

	return (x, y)

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
															"%s%sBL" % (xString, yString)]]
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
															"%s%sCC" % (xString, yString)]]
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
															"%s%sTL" % (xString, yPString)]]
		br = ["%s%sBR" % (xString, yString), 0.75, 0.75, [	"%s%sBL" % (xPString, yString),
															"%s%sTR" % (xString, yString)]]
		cc = ["%s%sCC" % (xString, yString), 0.50, 0.50, [	"%s%sTR" % (xString, yString),
															"%s%sBL" % (xString, yString),
															"%s%sBR" % (xString, yString)]]

	pointList = [tl, tr, bl, br, cc]

	return pointList

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
		start = 0.0
		end = 90.0

		enterIn =	["%s%sTL" % (xPString, yString), 0.25, 0.25, ["%s%sI0" % (xString, yString)]]
		enterOut =	["%s%sBL" % (xString, yPString), 0.25, 0.75, ["%s%sO0" % (xString, yString)]]
		exitIn =	["%s%sTL" % (xString, yPString), 0.25, 0.25, ["%s%sTR" % (xMString, yPString)]]
		exitOut =	["%s%sTR" % (xPString, yString), 0.75, 0.25, ["%s%sBR" % (xPString, yMString)]]

		endIn = "%s%sTL" % (xString, yPString)
		endOut = "%s%sTR" % (xPString, yString)

	elif type == 9:			# Bottom left
		centerX = 103.0 / 64.0
		centerY = 25.0 / 64.0
		start = 90.0
		end = 180.0

		enterIn =	["%s%sTR" % (xPString, yPString), 0.25, 0.75, ["%s%sI0" % (xString, yString)]]
		enterOut =	["%s%sTL" % (xString, yString), 0.25, 0.25, ["%s%sO0" % (xString, yString)]]
		exitIn =	["%s%sTR" % (xString, yString), 0.25, 0.75, ["%s%sBR" % (xString, yMString)]]
		exitOut =	["%s%sBR" % (xPString, yPString), 0.75, 0.75, ["%s%sBL" % (xPPString, yPString)]]

		endIn = "%s%sTR" % (xString, yString)
		endOut = "%s%sBR" % (xPString, yPString)

	elif type == 10:		# Top left
		centerX = 103.0 / 64.0
		centerY = 103.0 / 64.0
		start = 180.0
		end = 270.0

		enterIn =	["%s%sBR" % (xString, yPString), 0.75, 0.75, ["%s%sI0" % (xString, yString)]]
		enterOut =	["%s%sTR" % (xPString, yString), 0.75, 0.25, ["%s%sO0" % (xString, yString)]]
		exitIn =	["%s%sBR" % (xPString, yString), 0.75, 0.75, ["%s%sBL" % (xPPString, yString)]]
		exitOut =	["%s%sBL" % (xString, yPString), 0.25, 0.75, ["%s%sTL" % (xString, yPPString)]]

		endIn = "%s%sBR" % (xPString, yString)
		endOut = "%s%sBL" % (xString, yPString)

	else: # type == 11:		# Top right
		centerX = 25.0 / 64.0
		centerY = 103.0 / 64.0
		start = 270.0
		end = 360.0

		enterIn =	["%s%sBL" % (xString, yString), 0.75, 0.75, ["%s%sI0" % (xString, yString)]]
		enterOut =	["%s%sBR" % (xPString, yPString), 0.75, 0.75, ["%s%sO0" % (xString, yString)]]
		exitIn =	["%s%sBL" % (xPString, yPString), 0.25, 0.75, ["%s%sTL" % (xPString, yPPString)]]
		exitOut =	["%s%sBR" % (xString, yString), 0.25, 0.25, ["%s%sTR" % (xMString, yString)]]

		endIn = "%s%sBL" % (xPString, yPString)
		endOut = "%s%sTL" % (xString, yString)

	pointList = [enterIn, enterOut, exitIn, exitOut]

	string = "%s%s" % (xString, yString)
	step = ((end - 10.0) - (start + 10.0)) / float(slices)

	for i in range(slices):

		angle = radians(start + step * i)

		if i < 9:
			temp = ["%sI%d" % (string, i), centerX + cos(angle) * innerRadius,
													centerY + sin(angle) * innerRadius,
													["%sI%d" % (string, i + 1)]]
		else:
			temp = ["%sI%d" % (string, i), centerX + cos(angle) * innerRadius,
													centerY + sin(angle) * innerRadius,
													[endIn]]

		pointList.append(temp)

		angle = radians(start + step * (10 - i))

		if i < 9:
			temp = ["%sO%d" % (string, i), centerX + cos(angle) * outerRadius,
													centerY + sin(angle) * outerRadius,
													["%sO%d" % (string, i + 1)]]
		else:
			temp = ["%sO%d" % (string, i), centerX + cos(angle) * outerRadius,
													centerY + sin(angle) * outerRadius,
													[endIn]]

		pointList.append(temp)

	return pointList

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

	pointList = [tl, tr, bl, br]

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

	pointList = [tl, tr, bl, br]

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

	pointList = [tl, tr, bl, br, cc]

	return pointList

if __name__ == "__main__":
	main()
