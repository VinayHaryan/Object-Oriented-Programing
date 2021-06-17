'''
Classes
Just like every other Object Oriented Programming language Python supports classes. 
Let’s look at some points on Python classes.

Classes are created by keyword class.
Attributes are the variables that belong to class.
Attributes are always public and can be accessed using dot (.) operator. Eg.: Myclass.Myattribute

'''

# create a class named MyClass
class myclass:
    # assign the values to the myclass attrubutes
    number = 0
    name = "noname"

def main():
    # creating an object of the myclass
    # here me is the object
    me = myclass()

    # accessing the attributes of myclass
    # using the dot(.) operator
    me.number = 1337
    me.name = "vinay"

    # str is an build-in function that
    # create an string
    print(me.name + " " + str(me.number))

# telling python that there is main in the program
if __name__ == "__main__":
    main()


'''
Methods
Method is a bunch of code that is intended to perform a particular task in your Python’s code.

Function that belongs to a class is called an Method.

All methods require ‘self’ parameter. If you have coded in other OOP language you can think of ‘self’ as the ‘this’ keyword 
which is used for the current object. It unhides the current instance variable.’self’ mostly work like ‘this’.

‘def’ keyword is used to create a new method.

'''
# a python program to demonstrate working of class method
class vector2D:
    x = 0.0
    y = 0.0

    # creating a method named set
    def sett(self,x,y):
        self.x = x
        self.y = y

def main():
    vec = vector2D()

    # passing values to the function set
    # by using dot(.) operator
    vec.sett(5,6)
    print("x: "+str(vec.x) + ", Y:" + str(vec.y))

if __name__ == "__main__":
    main()


'''
Inheritance
Inheritance is defined as a way in which a particular class inherits features from its base class.Base class is also knows as ‘Superclass’ and the class which inherits from the Superclass is knows as ‘Subclass’

# Syntax for inheritance
  
class derived-classname(superclass-name)

'''
# A Python program to demonstrate working of inheritance
class Pet:
        #__init__ is an constructor in Python
        def __init__(self, name, age):     
                self.name = name
                self.age = age
  
# Class Cat inheriting from the class Pet
class Cat(Pet):         
        def __init__(self, name, age):
                # calling the super-class function __init__ 
                # using the super() function
                super().__init__(name, age) 
  
def Main():
        thePet = Pet("Pet", 1)
        jess = Cat("Jess", 3)
          
        # isinstance() function to check whether a class is 
        # inherited from another class
        print("Is jess a cat? " +str(isinstance(jess, Cat)))
        print("Is jess a pet? " +str(isinstance(jess, Pet)))
        print("Is the pet a cat? "+str(isinstance(thePet, Cat)))
        print("Is thePet a Pet? " +str(isinstance(thePet, Pet)))
        print(jess.name)
  
if __name__=='__main__':
        Main()

'''
Iterators

Iterators are objects that can be iterated upon.

Python uses the __iter__() method to return an iterator object of the class.

The iterator object then uses the __next__() method to get the next item.

for loops stops when StopIteration Exception is raised.

'''
# this program will reverse the string that is passed
# to it form the main function
class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def Main():
    rev = Reverse("Drapsicle")
    for char in rev:
        print(char)

if __name__ == "__main__":
    Main()


'''
Generators

Another way of creating iterators.

Uses a function rather than a separate class

Generates the background code for the next() and iter() methods

Uses a special statement called yield which saves the state of the generator and set a resume point for when next() is called again.

'''  
def Reverse(data):
    # this is like counting from 100 to 1 by taking one(-1)
    # step backward
    for index in range(len(data)-1,-1,-1):
        yield data[index]

def main():
    rev = Reverse("vinay")
    for char in rev:
        print(char)
    

if __name__ == "__main__":
    main()