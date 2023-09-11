#inheritance

class polygoan():
    def __init__(self, sides):
        self.sides=sides
    
    def display_info(self):
        print("A polygoan is a two dimensional shape with two straight lines")
    
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
    
class triangle(polygoan):
    def display_info(self):
        print("A triangle is a polygoan with 3 sides")

        polygoan.display_info(self) # polygoan is the name of the parent class since, we'r csalling them the method of  rather than the objec pass explicity.t
        super().display_info()# super fn return temporary object of the super class forz sub class. super is an object of polygon in this example.
class quadrilateral(polygoan): 
    def display_info(self):
        print("A quadrilateral is a polygoan with 4 sides")

t1=triangle([5,6,7])
perimeter=t1.get_perimeter()
print(perimeter)
# t1.display_info()