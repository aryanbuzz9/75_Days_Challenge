# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def cal_area(self):
        return math.pi*(self.radius**2)

# obj=Circle(3)
# print(math.floor(obj.cal_area()))

# Write a Python program to create a person class. Include attributes like name, country and 
# date of birth. Implement a method to determine the person's age.

class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob

    # def cal_age(self):
