class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def __len__(self):
        return self.length
    
    def add_node(self,data):
        new_node = Node(data)
        new_list = [new_node]
        new_list.append(data)
        self.head = new_node
        self.length += 1

        
        
        

    