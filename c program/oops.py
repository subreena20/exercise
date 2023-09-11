# class empolyee:
#     pass

# class Dogs: # class is a keyword and dogs is a classname.
#     pass                           #pass is used when we want to run our program without exception vn we don't know code.ss
# D1=Dogs()
# print(D1)
# print(id(D1))

# class Dogs:
#     def __init__(self,name,color,age):
#         self.name=name
#         self.color=color 
#         self.age=age
#     def barking(self):
#         print("Woof Woof")


#property based descriptors.

# class circle:
#     def __init__(self, radius):
#         self.radius=radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         if isinstance(value,str) or (value<=0):
#             raise ValueError("positive number excepted")
#         self._radius=value 
# # ob=circle(12)
# ob=circle("subreena")

# Lightweight classes.
#    with __slots__

# class points:
#     __slots__=("x","y")
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y

#     def distance(s1,s2):
#         d=(s2.x - s1.x)**2 + (s2.y - s1.y)**2
#         print(d**0.5)
# p1=points(3,4)
# p2=points(8,7)

# # p1.z=43

# from pympler import asizeof
# print(asizeof.asizeof(p1))
# p1.distance(p2)
# p2.distance(p1)

class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def __str__(self):
        return(f"this is a {self.make}, {self.model} car")
   
# c2=car("abcd", "s1df", 2023)
# print(c2)
    def __repr__(self):
        return(f"make={self.make}, model={self.model}, year={self.year}")