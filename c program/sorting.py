import random, time

def bubble_sort(a):
    b=len(a)
    for i in range(b):
        for j in range(b-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a 

d={"bubble":[0,0,0,0,0],
    "Selection":[0,0,0,0,0],
      "insertion" :[0,0,0,0,0],
      "quick":[0,0,0,0,0] ,
      " merge":[0,0,0,0,0]}

nl=10
for _ in range(4):
    # n=10
    l=[0]*nl
    for k in range(nl):
        num=random.randint(1,nl+1)
        l[k]=num
 
    start=time.time()
    bubble_sort(l)
    end=time.time()

    d['bubble'][_]=end-start
    nl=nl*10
print(d)
