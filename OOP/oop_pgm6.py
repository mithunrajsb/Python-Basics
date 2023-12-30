# private members

class A:
    def set(self,x,y):
        self.x = x
        self.__y = y
    
    def print(self):
        print("{} {}".format(self.x,self.__y))


a = A()
a.set(3,4)
a.print()

print(a.x)
print(a.__y)  #AttributeError: 'A' object has no attribute '__y'