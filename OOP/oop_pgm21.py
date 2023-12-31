# getattr
# getattr(object,attribute,[,default])

class A:
    def __init__(self) :
        self.x = 0
    
    
    
a = A()
print(getattr(a,'x',2))
print(getattr(a,'y',2)) # returns 2 (default), as there is no attribute y
# print(getattr(a,'y')) # Error


