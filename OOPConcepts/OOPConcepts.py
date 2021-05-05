# classes are user defined blueprint or prototype
# will have methods, class variables, instance variables, constructor etc.

# declaring class in Python
class Calculator:
    num = 100



    # declaring method in class
    def getData(self):
        print("I am now executing as method in class")


# creating object in python

 # Constructor is one method which is automatically called when you create object for any class


obj = Calculator() # syntax to create objects in python
obj.getData()
print(obj.num)