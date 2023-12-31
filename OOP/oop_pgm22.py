# setattr
# setattr(object,attribute,value)

class A:
    def __init__(self) :
        self.x = 0
    
    
    
a = A()
setattr(a,'x',2)
setattr(a,'y',6)

print(getattr(a,'x',1))
print(getattr(a,'y',2)) 



