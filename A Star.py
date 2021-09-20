import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=300)
import time

import pandas as pd
from PIL import Image

def main():
    OpenList = [[1,-1,1,1],[1,1,1,1],[1,1,1,1]]               
    ClosedList = []             #List of Nodes we have already visited and collected all their neighbors
    print(GetNeigbors(OpenList, [1,15]))
    
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


     
main()
