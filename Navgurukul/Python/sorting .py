#linear searching
def search(array,key):
    for i in range(n):
        if array[i]==key:
            return True
    return False 
array=[10,50,30,70,80,60,20,90,40]
n=len(array)
print(search(array,80))
