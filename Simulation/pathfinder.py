import map_to_points

def findPath(startNode, endNode, nodeDict, distDict):
	"""An implementation of the classic A* algorithm."""

	# Open list is tuples of (f, g, h, name, parent)
	# Closed list is tuples of closed stuff
	# OpenCheck is a list of names (so we can figure out if a node is open)
	# ClosedCheck is just names

	# First we set things up.

	startToEnd = getDistance(startNode, endNode, nodeDict, distDict)

#	print ""
#	print "\tAsked to find path from '%s' to '%s' which are %f apart." % (startNode, endNode, startToEnd)

	openList = [(startToEnd, 0.0, startToEnd, startNode, "")]
	openCheck = {}
	openCheck[startNode] = startToEnd
	closedList = []
	closedCheck = {}

	# Now we check for the trivial case

	if startNode == endNode:
		return []	# No path needed, you're there

#	print "\tStart and end nodes are different. Dang."

	thereYet = False

	while not thereYet:

		if openList == []:
			# Out of nodes, we're done
			print "WARNING: NO PATH FOUND BETWEEN '%s' AND '%s'!!!" % (startNode, endNode)
#			print "\t\tOut of nodes! We're returning."
#			print ""
			return []

		openList.sort()
		bestChance = openList.pop(0)
		(nodeF, dist, nodeH, name, nodeParent) = bestChance
		closedList.append(bestChance)
		closedCheck[name] = nodeParent
		del openCheck[name]

#		print "\t\tLooking at node '%s'..." % (name)

		if (name == endNode):
			thereYet = True
#			print "\t\tFound the end node!"
			break

		newOpen = nodeDict[name]
		newOpenList = newOpen[2]

		for node in newOpenList:
			g = dist + getDistance(name, node, nodeDict, distDict)
			h = getDistance(node, endNode, nodeDict, distDict)

			if not closedCheck.has_key(node):
				if not openCheck.has_key(node):
					openList.append((g + h, g, h, node, name))
					openCheck[node] = g + h

	# By now we've found a path, ending at the end node. No we just work backwards!

#	print "\tLooking backwards..."

	path = [endNode]

	while True:

		previousNode = path[len(path) - 1]
		nextNode = closedCheck[previousNode]

#		print "\t\t'%s' -> '%s'..." % (previousNode, nextNode)

		if nextNode == startNode:
			break

		path.append(nextNode)

	# Now reverse it

	path.reverse()

#	print "\tFound path."
#	print ""

	return path	# This should do it

def getDistance(nodeOne, nodeTwo, nodeDict, distDict):
	"""Get the distance between two nodes, using a table if possible."""

	if (nodeOne == nodeTwo):
		return 0.0
	elif (nodeOne < nodeTwo):
		name = "%s%s" % (nodeOne, nodeTwo)
	else:
		name = "%s%s" % (nodeTwo, nodeOne)

	if distDict.has_key(name):
		return distDict[name]
	else:
		distance = map_to_points.distanceBetween(nodeOne, nodeTwo, nodeDict)
		distDict[name] = distance
		return distance