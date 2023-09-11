# list=["spider","thor","hulk","idron man","captain american"]
# print(len(list))
# list.append("black panther")
# print(list)
# list.remove("captain american")
# print(list)
# list.insert(3,"captain american")
# print(list)
# n=int(input())
# i=0
# c=0
# while i<n:
#     c=c+1
#     i+=1
# print(c)

# user=int(input("enter a number: "))
# i=1
# list=[]
# for i in range(1,user+1,2):

#     list.append(i)
# print(max(list)) 

# n=123 
# while n>0:
#     n=n//10 
# print(n)



for i in range(3,432):
    a=i
    f=0
    while i>=10:
        i=i//10 
    # print(i)
    f+=i
    l=(a%10) 
    # print(l)
    c=0
    if f==l:
        print(a)
print(c)
