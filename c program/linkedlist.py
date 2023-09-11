# creating a linked list.
class linkedlist:
    def __init__(self):
        self.head=None

    def __repr__(self):
        node=self.head
        nodes=[]
        while node !=None:
            nodes.append(node.data)
            node=node.next
        nodes.append("None")
        return "->".join(nodes)
    
            
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data