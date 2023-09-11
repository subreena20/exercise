# a=[9,7,3,1,8,4,12,6]
# n=len(a)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if a[j]<a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# def bubble_sort(a,n):
#     # n=len(a)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return a 
# a=list(map(int,input().split()))
# a=bubble_sort(a,5)
# print(a)

#selection sort.

# a=[9,7,3,1,8,4,12,6]
# n=len(a)
# for i in range(n-1): 
#     min_index=i 
#     for j in range(i+1,n):
#         if a[j]<a[min_index]:
#             min_index=j 
#     a[i],a[min_index]=a[min_index],a[i]
# print(a)

# def selection(a):
#     n=len(a)
#     for i in range(n-1): 
#         min_index=i 
#         for j in range(i+1,n):
#             if a[j]<a[min_index]:
#                 min_index=j 
#         a[i],a[min_index]=a[min_index],a[i]

# a=list(map(int,input().split()))
# selection(a)
# print(a)


#insertion sort

# a=[3,8,9,6,2,7]
# n=len(a) 
# for i in range(1,n):
#     key=a[i]
#     j=i-1
#     while j>=0 and key < a[j]:
#         a[j+1]=a[j]
#         j=j-1
#     a[j+1]=key
# print(a) 


# def insertion_sort(a):
#     n=len(a)
#     for i in range(1,n):
#         key=a[i]
#         j=i-1
#         while j>=0 and key < a[j]:
#             a[j+1]=a[j]
#             j=j-1
#         a[j+1]=key
#     return a 
# a=[3,8,9,6,2,7]
# insertion_sort(a)
# print(a)


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
a=[65,45,12,80,86,5,7,35]
n=len(a)
quick_sort(a,0,n-1)
print(a)

#Mergesort.
def mergesort(a):
    if len(a)>1:
        mid=len(a)//2 
        sa1=a[ :mid]
        sa2=a[mid: ]
        mergesort(sa1)
        mergesort(sa2)
        i=j=k=0
        while i<len(sa1) and j<len(sa2):
            if sa1[i]<sa2[j]:
                a[k]=sa1[i]
                i=i+1
            else:
                a[k]=sa2[j]
                j=j+1
            k+=1
        while i<len(sa1):
            a[k]=sa1[i]
            i+=1
            k+=1
        while j<len(sa2):
            a[k]=sa2[j]
            k+=1
            j+=1
a=[13,9,12,6,8,15,3,2]
print(mergesort(a))
