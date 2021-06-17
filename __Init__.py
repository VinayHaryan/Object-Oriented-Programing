'''
__init__ in Python

Prerequisites – Python Class, Objects, Self

Whenever object oriented programming is done in Python, 
we mostly come across __init__ method which we usually don’t fully understand. 
This article explains the main concept of __init__ but before understanding the __init__ 
some prerequisites are required.

__init__

The __init__ method is similar to constructors in C++ and Java. 
Constructors are used to initialize the object’s state. 
The task of constructors is to initialize(assign values) 
to the data members of the class when an object of class is created. 
Like methods, a constructor also contains collection of statements(i.e. instructions) 
that are executed at time of Object creation. 
It is run as soon as an object of a class is instantiated. 
The method is useful to do any initialization you want to do with your object.


'''
# simple class with init method
class person:
    # init method or constructor
    def __init__(self,name):
        self.name = name

    # simple Method
    def say_hi(self):
        print("Hello, my name is",self.name)

p = person('vinay')
p.say_hi()

class A(object):
    def __init__(self, something):
        print("a init called")
        self.something = something

class B(A):
    def __init__(self, something):
        A.__init__(self,something)
        print("B init called")
        self.something = something


obj = B('something')

