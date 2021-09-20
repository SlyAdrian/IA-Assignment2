import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=300)
import time

import pandas as pd
from PIL import Image

def main():
    OpenList = [[1,-1,1,1],[1,1,1,1],[1,1,1,1]]               
    ClosedList = []             #List of Nodes we have already visited and collected all their neighbors
    print(GetNeigbors(OpenList, [1,1]))
    print(get_neighbours(OpenList, [1,1]))
    
    pass

#Takes the Map and Coordinate and returns its Valid Neighbors in a List with their Values
def GetNeigbors(Map, Coordinate):
    Neighbors = []
    if len(Map) <= 0:
        return []
    NeighborCoordinate = [Coordinate[0],Coordinate[1] -1]         #Above
    if 0 <= NeighborCoordinate[0] <= len(Map) and 0 <= NeighborCoordinate[1] <= len(Map[NeighborCoordinate[0]]):
            if Map[NeighborCoordinate[0]][NeighborCoordinate[1]] >= 0:
                Neighbors.append(NeighborCoordinate)
        
    NeighborCoordinate = [Coordinate[0],Coordinate[1] +1]         #Below
    if 0 <= NeighborCoordinate[0] <= len(Map) and 0 <= NeighborCoordinate[1] <= len(Map[NeighborCoordinate[0]]):
            if Map[NeighborCoordinate[0]][NeighborCoordinate[1]] >= 0:
                Neighbors.append(NeighborCoordinate)
        
    NeighborCoordinate = [Coordinate[0] -1, Coordinate[1]]         #Left
    if 0 <= NeighborCoordinate[0] <= len(Map) and 0 <= NeighborCoordinate[1] <= len(Map[NeighborCoordinate[0]]):
            if Map[NeighborCoordinate[0]][NeighborCoordinate[1]] >= 0:
                Neighbors.append(NeighborCoordinate)
        
    NeighborCoordinate = [Coordinate[0] +1, Coordinate[1]]         #Right
    if 0 <= NeighborCoordinate[0] <= len(Map) and 0 <= NeighborCoordinate[1] <= len(Map[NeighborCoordinate[0]]):
            if Map[NeighborCoordinate[0]][NeighborCoordinate[1]] >= 0:
                Neighbors.append(NeighborCoordinate)
        
    return Neighbors

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
     
main()
