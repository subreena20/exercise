class Node:
    def __init__(s,v):
        s.value=v
        s.next=None
class ll:
    def __init__(s):
        s.head=None
    def display(s):
        p=s.head
        while p.next!=None:
            print(p.value,end="->")
            p=p.next
        print(p.value,end='->')
        print(p.next)

    def insertatbegin(s,val):
        new=Node(val)
        new.next=s.head
        s.head=new
        
    def totalele(s):
        p=s.head
        c=0
        while p.next!=None:
            c+=1
            p=p.next


    def middleele(s):
        p1=s.head
        p2=s.head
        while p2.next!=None:
            p2=p2.next.next
            p1=p1.next
        print(p1.value)