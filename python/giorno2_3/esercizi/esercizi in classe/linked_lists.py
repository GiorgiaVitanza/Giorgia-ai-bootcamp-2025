class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
        

    def __len__(self):
        return self.length

    def __iter__(self):
        return iter([self.head, self.head.next])
   
        
    
    def add_node(self,data=""):  
         new_node = Node(data)
         if self.head is None:
            self.head = new_node
            self.length += 1
         else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        

         return [new_node, new_node.next]
        
        
            
                
        
        

        
        
        

    