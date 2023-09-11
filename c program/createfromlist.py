class NOde:
    def __init__(s,v):
        s.value=v

def createfromlist(s,l):
    l=list(map(int,l.split()))
    s.head=Node(l[0])
    p=s.head
    for i in range(1,len(l)):
        p.next=Node(l[i])
        p=p.next