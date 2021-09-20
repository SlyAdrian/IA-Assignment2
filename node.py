class Node:
    def __init__(self, f_value = 0, path_cost = 0 , open = True , location = [0,0]):
        self.f_value = f_value
        self.path_cost = path_cost
        self.open = open
        self.location = location

    def set_f_value(self, f_value):
        self.f_value = f_value

    def set_path_cost(self, path_cost):
        self.path_cost = path_cost

    def set_open(self, open):
        self.open = open
    
    def set_location(self, location):
        self.location = location

    def get_attributes(self):
        print(f'f value : {self.f_value}\t path cost : {self.path_cost}\t open : {self.open}\t location : {self.location}')

n1 = Node(15, 10, True, [0,1])
print(n1.get_attributes())
n1.set_location(location=[1,2])
print(n1.get_attributes())

