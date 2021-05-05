# Constructor is one method which is automatically called when you create object for any class
# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100  # class variables

    # default constructor
    def __init__(self, a, b): # ignore self
        # instance variables
        self.a = a
        self.b = b
        print ("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.a + self.b + Calculator.num


obj = Calculator(2, 3)  # syntax to create objects in python
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)  # syntax to create objects in python
obj1.getData()
print(obj1.summation())
