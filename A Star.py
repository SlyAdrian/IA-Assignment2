import numpy as np
import time

from Map import Map_Obj
import pandas as pd

from PIL import Image



np.set_printoptions(threshold=np.inf, linewidth=300)

def main():
    print("Start of the A*")

    #### TASK 1 ####

    # Initialization of the map 
    
    # Initialization of the 2 lists
    openList = []
    closedList = []
    
    task1 = Map_Obj(task=1)

    # Beginning of the algorithm
    openList.append(task1.get_start_pos)

""" def main():    
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
			
    
    pass """

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

     
main()
