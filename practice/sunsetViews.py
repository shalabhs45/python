def sunsetViews(buildings, direction):
    # Write your code here.
	buildViews = []
	startIDx = 0 if direction == "EAST" else len(buildViews) -1
	step = 1 if direction == "EAST" else -1
	idx = startIDx
	while idx >=0 and idx < len(buildings):

		buildingHeight = buildings[idx]
		print("Reading Element", buildingHeight)
		while len(buildViews) > 0 and buildings[buildViews[-1]] <= buildingHeight:
                   print('poping {0}'.format(buildViews[-1]))
                   buildViews.pop()	
		buildViews.append(idx)
		
		idx += step	
	if direction == "WEST":
		return buildViews[::-1]
	return buildViews
	
print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2],"WEST"))
