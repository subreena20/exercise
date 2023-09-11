# import time
# start= time.time()
# i=0
# n=10**7 
# while i<n:
#     i+=1 
#     end=time.time()
# print(end-start)

# generating a numbers randomly.
# import random

# # n=random.randint(2,10)
# # print(n)
# l=[0]*10
# for i in range(10):
#     n=random.randint(1,11)
#     l[i]=n 
# print(l)

import random, time

def bubble_sort(a):
    b=len(a)
    for i in range(b):
        for j in range(b-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a 

def selection(a):
    n=len(a)
    for i in range(n-1): 
        min_index=i 
        for j in range(i+1,n):
            if a[j]<a[min_index]:
                min_index=j 
        a[i],a[min_index]=a[min_index],a[i]
    return a

def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        key=a[i]
        j=i-1
        while j>=0 and key < a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a 

def partition(a,low,high):
    pivot=a[high]
    i=low-1
    for j in range(low,high):
        if a[j]<=pivot:
            i=i+1
        a[i],a[j]=a[j],a[i]
    a[i+1],pivot=pivot,a[i+1]
    return i+1
def quick_sort(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        quick_sort(a,low,pi-1)
        quick_sort(a,pi+1,high)



d={"bubble":[0,0,0,0,0],
    "Selection":[0,0,0,0,0],
      "insertion" :[0,0,0,0,0],
      "quick":[0,0,0,0,0] ,
      " merge":[0,0,0,0,0]}

nl=10
for _ in range(5):
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


