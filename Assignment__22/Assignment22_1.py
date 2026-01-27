
#######################################################################################
#           
# Description : Write a Python program to implement a class named Demo with the 
#               following specifications:
#               The class should contain two instance variables: no1 and no2.
#               The class should contain one class variable named Value.
#               Define a constructor (__init__) that accepts two parameters and 
#               initializes the instance variables.
#               Implement two instance methods:
#               Fun() – displays the values of instance variables no1 and no2.
#               Gun() – displays the values of instance variables no1 and no2
#
########################################################################################
class Demo:
    Value = 0

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
    
    def Fun(self):
        print("No1 :",self.No1)
        print("No2 :",self.No2)

    def Gun(self):
        print("No1 :",self.No1)
        print("No2 :",self.No2)

obj1 = Demo(11,21)

obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()