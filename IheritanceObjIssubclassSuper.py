'''
OOP in Python | Set 3 (Inheritance, examples of object, issubclass and super)

In this article, Inheritance is introduced.

One of the major advantages of Object Oriented Programming is re-use. 
Inheritance is one of the mechanisms to achieve the same. 
In inheritance, a class (usually called superclass) is inherited by another class (usually called subclass). 
The subclass adds some attributes to superclass.

Below is a sample Python program to show how inheritance is implemented in Python.

'''
# a python program to demonstrate inheritance
# base or super class. Note object in bracket
# (Generally, object is made ancestor of all classes)
# equivalent to "class person(object)"

class Person(object):

    # constructor 
    def __init__(self, name):
        self.name = name

    # to get name
    def getname(self):
        return self.name

    # to check if this person is employee
    def isEmployee(self):
        return False

# inherited or sub class (note person in bracket)
class Employee(Person):

    # here we return true 
    def isEmployee(self):
        return True


# Drived code
emp = Person("Geek1")  # an object of person
print(emp.getname(), emp.isEmployee())

emp = Employee("Geek2")
print(emp.getname(), emp.isEmployee())

'''
How to check if a class is subclass of another?
Python provides a function issubclass() that directly tells us if a class is subclass of another class.
'''
# python example to check if a class is subclass of another
class Base(object):
    pass

class Derived(Base):
    pass

# Driver code
print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))

# but d is an instance of Base
print(isinstance(d,Base))

'''
what is object class

Like Java Object class, in Python (from version 3.x), object is root of all classes.

In Python 3.x, “class Test(object)” and “class Test” are same.
In Python 2.x, “class Test(object)” creates a class with object as parent (called new style class) 
and “class Test” creates old style class (without object parent). Refer this for more details.

Does Python support Multiple Inheritance?
Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as comma separated list in bracket.

Does Python support Multiple Inheritance?
Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as comma separated list in bracket.

'''
# python example to show working of multiple inheritance
class base1(object):
    def __init__(self):
        self.str1 = "geek1"
        print("base1")

class base2(object):
    def __init__(self):
        self.str2 = "geek2"
        print("base2")

class Derived(base1, base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("Derived")

    def printstrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printstrs()

# How to acess parent members in a subclass
# 1.using Parent class name
# show that base members can be accessed in derived class using base class name

class Base(object):
    # constructor
    def __init__(self,x):
        self.x = x

class Derived(Base):
    # constructor
    def __init__(self,x,y):
        Base.x = x
        self.y = y

    def printxy(self):
        # print (self.x, self.y) will also work
        print(Base.x, self.y)

# Deriver Code
d = Derived(10,20)
d.printxy() 


# using super()
# we can also access parent class members using super
# derived class using super

class Base(object):
    # constructor 
    def __init__(self,x):
        self.x = x

class Derived(Base):
    # in python 3.x "super()".__init__(name) also works
    def __init__(self,x,y):
        # in python 3.x super().__init__(name) also work
        super(Derived,self).__init__(x)
        self.y = y

    def printxy(self):

        # note that base.x won't work here
        # because super() is used in constructor
        print(self.x, self.y)

d = Derived(10,20)
d.printxy()

'''
Note that the above two method are not exactly same.
in the next article on inheritance, we will convering following topis
1) how super works? how acessing a member through super and parent class name are different?
2) how Diamond probleam is handled in python
'''

class X(object):
    def __init__(self, a):
        self.num = a
    def doubleup(self):
        self.num *= 2
  
class Y(X):
    def __init__(self, a):
        X.__init__(self, a)
    def tripleup(self):
        self.num *= 3
  
obj = Y(4)
print(obj.num)
  
obj.doubleup()
print(obj.num)
  
obj.tripleup()
print(obj.num)

# Base or Super class
class Person(object):
    def __init__(self, name):
        self.name = name
          
    def getName(self):
        return self.name
      
    def isEmployee(self):
        return False
  
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    def __init__(self, name, eid):
  
        ''' In Python 3.0+, "super().__init__(name)"
            also works''' 
        super(Employee, self).__init__(name)
        self.empID = eid
          
    def isEmployee(self):
        return True
          
    def getID(self):
        return self.empID
  
# Driver code
emp = Employee("Geek1", "E101") 
print(emp.getName(), emp.isEmployee(), emp.getID())
