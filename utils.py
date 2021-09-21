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

# Takes the Map and Coordinate and returns its Valid Neighbors in a List with their Values
def get_neighbours(map, location):
    assert len(map) > 0 and location[0] in range(0, len(map)) and location[1] in range(0, len(map[0])), "Initial location is not within the map range"

    neighboors = []

    line_range = range(0, len(map))
    column_range = range(0, len(map[location[0]]))
    
    x = location[0]
    y = location[1]

    # Above     
    if y-1 in column_range :
        if map[x][y-1] >= 0:
            neighboors.append([x, y-1])

    # Below
    if y+1 in column_range :
        if map[x][y+1] >= 0:
            neighboors.append([x, y+1])
    # Left
    if x-1 in line_range :
        if map[x-1][y] >= 0:
            neighboors.append([x-1, y])
    
    # Right
    if x+1 in line_range :
        if map[x+1][y] >= 0:
            neighboors.append([x+1, y])
    
    return neighboors

def FValue(Coordinate):
    #Must be implemented
    return

# Only work for maps that 
def create_open_list_2D(map):
    return [[False for j in range(len(map[0]))] for i in range(len(map))]

# Returns true if the element is in the list of nodes
def is_present(location, list):
    for n in list:
        if n.location == location:
            return True

    return False 
