import numpy as np
import time
import pandas as pd

from PIL import Image
from Map import Map_Obj


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

    pass


main()
