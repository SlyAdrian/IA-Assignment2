from node import Node

# Sorting function using bubble sort
def sort_nodes(list):

    n = len(list)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j].f_value > list[j + 1].f_value :
                list[j], list[j + 1] = list[j + 1], list[j]

    return list



# Testing code

""" node1 = Node(location=[1,2], f_value = 5, path_cost= 2)
node2 = Node(location=[3,2], f_value = 2, path_cost= 4)
node3 = Node(location=[0,2], f_value = 3, path_cost= 1)
node4 = Node(location=[0,2], f_value = 10, path_cost= 1)

nodes_list = [node1, node2, node3, node4]
for x in nodes_list:
    print (x.__str__())

# print(nodes_list.__str__())

sorted_list = sort_nodes(nodes_list)
for x in sorted_list:
    print (x.__str__()) """