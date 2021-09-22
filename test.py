import numpy as np
import time

from Map import Map_Obj
import pandas as pd
from utils import create_open_list_2D, euclidian_distance, sort_nodes, get_neighbours
from PIL import Image
from node import Node


np.set_printoptions(threshold=np.inf, linewidth=300)

def main():
    print("Start of the A*")

    #### TASK 1 ####

    # Initialization of the map 
    
    task1 = Map_Obj(task=1)
    map= task1.get_maps()[0]
    map_str = task1.get_maps()[1]

    # Initialization of the 2 lists
    openList = []
    closedList = []

    # Creation of the false list to keep in memory the opened nodes
    openList2d = create_open_list_2D(map)

    # Beginning of the algorithm
    openList.append(Node(location=task1.start_pos, f_value = 0))

    # Safety counter
    i = 0

    while len(openList) != 0 :

        i+=1

        if i > len(map) * len(map[0]):
            return
            
        # Sorting of the openList to get the node with the lower f value as the first element of the list
        sort_nodes(openList)
        current = openList[0]
        print(i)
        print(current.location)
        print(openList)
        map_str[current.location[0]][current.location[1]] = ':'

        
        # Removal of the current node from the open list
        openList.remove(current)

        
        # Recovering of all the neighbours of the current node 
        neighbours = get_neighbours(map= map, location = current.location)
        

        for n in neighbours :
            
            # If n is the goal : stop
            if np.array_equal(n, task1.end_goal_pos) :

                end_node = Node(location= n, parent= current)

                openList.append(end_node)
                print(i)

                goal = task1.start_pos
                travelled = end_node

                # Display of the final path
                while travelled.location != goal:
                    
                    # Changing the colour of the travelled node
                    map_str[travelled.location[0]][travelled.location[1]] = ';'

                    travelled = travelled.parent

                return
            
            # Calculate neighbour g
            n_g = current.path_cost 

            # Calculate neighbour h 
            n_h = euclidian_distance(current= current.location, goal= task1.end_goal_pos)

            # Caluculate neighbour f
            n_f = n_g + n_h

            # Check whether the neighbour is already in the open list and if its f value if lower than neighbour's f value
            """ if is_present(n, openList) and n_f > openList.index(n):
                continue
            """
            if not isinstance(openList2d[n[0]][n[1]], bool) and openList2d[n[0]][n[1]].open :

                if n_f < openList2d[n[0]][n[1]].f_value :
                    openList2d[n[0]][n[1]].set_f_value(n_f)
                    openList2d[n[0]][n[1]].set_parent(current)
                else :    
                    continue

            # Check wheter the neighbour is already in the closed list and if its f value is lower thant neighbour's f value
            if not isinstance(openList2d[n[0]][n[1]], bool) and not openList2d[n[0]][n[1]].open :

                if n_f < openList2d[n[0]][n[1]].f_value :
                    openList2d[n[0]][n[1]].set_f_value(n_f)
                    openList2d[n[0]][n[1]].set_parent(current)
                else :    
                    continue
            
            # Otherwise add the neighbour to the openList
            new_node = Node(location= n, f_value= n_f, path_cost= n_g, open= True, parent= current)
            
            openList.append(new_node)

            # Updating of the openList2d with the reference of the new node added to open list
            openList2d[n[0]][n[1]] = new_node
            
        # Show the map of the path taken at each step
        """ task1.show_map(map= map_str) """

        # Add to the closed list
        closedList.append(current)

    # Display of the final path
    task1.show_map(map= map_str)

    
    
    
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
