import numpy as np
import time

from Map import Map_Obj
import pandas as pd
from utils import sort_nodes
from PIL import Image
from node import Node


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
    openList.append(Node(location=task1.get_start_pos, f_value = 0))

    while len(openList) != 0 :
        sort_nodes(openList)
        
    

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
     
main()
