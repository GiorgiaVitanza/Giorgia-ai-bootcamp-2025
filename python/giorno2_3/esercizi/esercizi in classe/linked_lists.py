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
        if self.head is None:
            # add the node head       
            self.head = Node(data) 
            # increase the length
            self.length += 1   
        else:
            # add next node
            self.head.next = Node(data)
            # new head
            self.head = Node(data)
            # increase the length
            self.length += 1  
        return [self.head,self.head.next]
            
                
        
        

        
        
        

    