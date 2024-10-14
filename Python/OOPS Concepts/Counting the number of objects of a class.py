class Person:
    count=0
    def __init__(self,name):
        self.name=name
        Person.count+=1

obj1=Person('Aryan')
print(Person.count)
obj2=Person('Python')
