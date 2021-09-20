import math

def manhattan_distance(current, goal) :
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def euclidian_distance(current, goal) :
    return math.sqrt((current[0] - goal[0])**2 + (current[1] - goal[1])**2)


