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

    def insertatend(s,val):
        new=Node(val)
        p=s.head
        while p.next!=None:
            p=p.next
        p.next=new

    def insertatpos(s,pos,val):
        newnode=Node(val)
        p=s.head
        i=1
        while i<pos-1:
            p=p.next
            i=i+1
        newnode.next=p.next
        p.next=newnode

    def removeatpos(s,pos):
        p=s.head
        i=0
        while i<pos-1:
            p=p.next
            i=i+1
        p.next=p.next.next
        s.display()

    def deletehead(s,key):
        p=s.head
        if p!= None and p.value==key:
            s.head=p.next