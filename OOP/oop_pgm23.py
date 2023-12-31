# delattr
# setattr(object,attribute)

class A:
    def __init__(self) :
        self.x = 0
    
    
    
a = A()
delattr(a,'x')  # attribute deleted


# print(getattr(a,'x'))  # Error
