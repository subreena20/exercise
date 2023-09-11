# class node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# n1=node(4)
# n2=node(6)
# n3=node(8)
# n4=node(10)
# n1.next=n2
# n2.next=n3
# n3.next=n4
# print(n1.next.next.next.value)
# p1=n1
# while p1.next!=None:
#     print(p1.value)
#     p1=p1.next


# class node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
#linkedlist
#     
# class ll(node):
#     def __init__(self):
#         self.head=None
#     def insert_at_beg(s):
#         n1=node(8)
#         p1=head
#         i=0
#         while i<3:
#             p1=p1.next
#             new_node.next=p1.next
#             p1.next=new_mode
#             i+=1
            
        
from collections import deque
deque()
print(deque)
deque('abcd')
print(deque)

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