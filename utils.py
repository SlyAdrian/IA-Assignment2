import math


def manhattan_distance(current, goal) :
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def euclidian_distance(current, goal) :
    return math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)

# Sorting function using bubble sort
def sort_nodes(list):

    n = len(list)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j].f_value > list[j + 1].f_value :
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

def FValue(Coordinate):
    #Must be implemented
    return

def CreateOpenList2D(Map):					#Creates A 2D Map of all the nodes for faster lookup whether we have found the Node already or not
	OpenList2D = []
	for i in range(len(Map)):
		OpenList2D.append([])
		for j in range(len(Map[i])):
			OpenList2D[i].append(False)
	#print(OpenList2D)
	return OpenList2D



