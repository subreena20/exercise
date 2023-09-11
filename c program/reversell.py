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
    def reversell(s):
        cur =s.head
        prev=None
        
        while cur!=None:
            nxt=cur.next
            cur.nxt=prev
            prev=cur
            cur=nxt
        s.head=cur


    def createfromlist(s,l):
        l=list(map(int,l.split()))
        s.head=Node(l[0])
        p=s.head
        for i in range(1,len(l)):
            p.next=Node(l[i])
            p=p.next 