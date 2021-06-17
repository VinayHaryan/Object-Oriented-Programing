'''
self in Python class

self represents the instance of the class. 
By using the “self” keyword we can access the attributes 
and methods of the class in python. It binds the attributes with the given arguments.


The reason you need to use self. 
is because Python does not use the @ syntax to refer to instance attributes. 
Python decided to do methods in a way that makes the instance to which the method belongs be passed 
automatically, but not received automatically: the first parameter of methods is the instance the method is called on.

'''
class check:
    def __init__(self):
        print("address of self= ",id(self))

o = check()
print("address of class object = ",id(o))


class car():

    # init method or constructor
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def show(self):
        print("model is", self.model)
        print("color is",self.color)

# both object have different self wich
# contain their attributes    
audi = car("audi a4",'blue')
ferrari = car('ferrari', 'green')

audi.show() # same output car.show(audi)
ferrari.show() # same output car.show(ferrari)
car.show(audi)

class use:
    def __init__(in_place_self):
        print("we have used another parameter name in place of self")


o = use()
