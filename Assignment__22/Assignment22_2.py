################################################################################################################
#
# Description : Write a Python program to implement a class named Circle with the following requirements:
#               The class should contain three instance variables: Radius, Area, and Circumference.
#               The class should contain one class variable named PI, initialized to 3.14.
#               Define a constructor (__init__) that initializes all instance variables to 0.0.
#               Implement the following instance methods:
#               Accept() – accepts the radius of the circle from the user.
#               CalculateArea() – calculates the area of the circle and stores it in the Area variable.
#               CalculateCircumference() – calculates the circumference of the circle and stores it in the 
#               Circumference variable.
#               Display() – displays the values of Radius, Area, and Circumference.
#               Create multiple objects of the Circle class and invoke all the instance methods for each object.
#
################################################################################################################

class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = int(input("Enter radius : "))

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius :",self.radius)
        print("Area :",self.area)
        print("Circumference :",self.circumference)
        
obj1 = Circle()
obj2 = Circle()
obj3 = Circle()

print("obj1 - ",end = "")
obj1.Accept()
print("obj2 - ",end = "")
obj2.Accept()
print("obj3 - ",end = "")
obj3.Accept()

obj1.CalculateArea()
obj2.CalculateArea()
obj3.CalculateArea()

obj1.CalculateCircumference()
obj2.CalculateCircumference()
obj3.CalculateCircumference()

print("obj1 - ",end = "")
obj1.Display()
print("obj2 - ",end = "")
obj2.Display()
print("obj3 - ",end = "")
obj3.Display()