
    # A member method that changes 
    # __hiddenvariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)



# Driver code
myobject = Myclass()
myobject.add(2)
myobject