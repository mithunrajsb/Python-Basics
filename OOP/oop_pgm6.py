# private members

class A:
    def set(self,x,y):
        self.x = x
        # __y is a private variable of the class
        self.__y = y
    
    def print(self):
        print("{} {}".format(self.x,self.__y))


a = A()
a.set(3,4)
a.print()

print("Value of a.x is",a.x)
#print(a.__y)  #AttributeError: 'A' object has no attribute '__y'