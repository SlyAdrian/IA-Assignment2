import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=300)
import time

import Map

import pandas as pd
from PIL import Image

def main():    
    object = Map.Map_Obj()            #Get the New Map
    map = object.read_map(path ="./Samfundet_map_1.csv")
    OpenList = []               #List of Nodes that we have not visited, but might want to
    ClosedList = []             #List of Nodes we have already visited and collected all their neighbors
    print(map[0])
    OpenList2D = CreateOpenList2D(map[0])
    CurrentCost = 0
    ClosedList.append(Node(map.get_start_pos(), 0, CurrentCost, True))       
    #A Star starts here:
    while(CONDITION):
        for N in GetNeighbors(map[0]):												#Iterate over Neighbors
            AdditionalCost = map[0][N[0]][N[1]]										#Get the Cost it takes for the Neighbor
            NewNeighbor = Node(N, F(N), CurrentCost +AdditionalCost, False)			#Create new node
			
    
    pass

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
