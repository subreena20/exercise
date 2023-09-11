#from collections import deque

class linkedlist:
    def __init__(self):
        self.head=None

    def __repr__(self):
        node= self.head
        nodes=[]
        while node is not None:
             nodes.append(node.data)
             node=node.next
        nodes.append("None")
        return "->".join(nodes)
        
    


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return self.data
    

# q2.
class linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        
        return " -> ".join(nodes)
    def __iter__(self):
       node = self.head
       while node is not None:
            yield node
            node = node.next
            
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data