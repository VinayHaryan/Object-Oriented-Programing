# Below is a simple Python program that creates a class with a single method. 
class Test:
    # a sample method
    def fun(self):
        print("hi")

o = Test()
o.fun()

'''
As we can see above, we create a new class using the class statement and the name of the class. 
This is followed by an indented block of statements that form the body of the class. 
In this case, we have defined a single method in the class.

Next, we create an object/instance of this class using the name of the class followed by a pair of parentheses.

Object:

The object is an entity that has a state and behavior associated with it. 
It may be any real-world object like the mouse, keyboard, chair, table, pen, etc. 
Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects. 
More specifically, any single integer or any single string is an object. The number 12 is an object, 
the string “Hello, world” is an object, a list is an object that can hold other objects, and so on. 
You’ve been using objects all along and may not even realize it.

Class:

A class is a blueprint that defines the variables and the methods (Characteristics) common to all objects of a certain kind.

Example: If Car is a class, then Audi A6 is an object of the Car class. All cars share similar features like 4 wheels, 
1 steering wheel, windows, breaks etc. Audi A6 (The Car object) has all these features.

 
The self 
 

Class methods must have an extra first parameter in the method definition. 
We do not give a value for this parameter when we call the method, Python provides it

If we have a method that takes no arguments, then we still have to have one argument – the self. 
See fun() in the above simple example.

This is similar to this pointer in C++ and this reference in Java.

When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.
method(myobject, arg1, arg2) – this is all the special self is about.


The __init__ method 
The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object. 

Here, we define the __init__ method as taking a parameter name (along with the usual self). .

'''
class person:
    # method or constructor
    def __init__(self,name):
        self.name = name

    def sayhi(self):
        print(self.name)
    
p = person("vinay")
p.sayhi()

'''
Class and Instance Variables (Or attributes) 
In Python, instance variables are variables whose value is assigned inside a constructor or method with self. 
Class variables are variables whose value is assigned in class.

'''
# python program to show that the variables with a value
# assigned in class declaration, are class variables and 
# variables inside method and constructors are instance variable
class elexstudent:
    # class variable 
    stream = 'Elex'

    # method or constructor
    def __init__(self,roll):

        # instance variable
        self.roll = roll


s1= elexstudent("100")
s2 = elexstudent("101")

print("\n")
print(s1.stream)
print(s2.stream)
print(s1.roll)

# class variables can be accessed using class name also
print(elexstudent.stream)

'''
We can define instance variables inside normal methods also.

'''
# python program to create that create instance variables insie method
class Electronics:
    # class variable 
    stream = 'ELEX'

    def __init__(self,roll):
        self.roll = roll
    
    def setaddress(self,add):
        self.add = add

    def getaddress(self):
        return self.add


s1 = Electronics("101")
s1.setaddress("Mumbai, Maharashatra")
print(s1.getaddress())

# create empty class
# an empty class
class Test:
    pass

    