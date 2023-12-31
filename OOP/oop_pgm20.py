# hassattr

class A:
    def __init__(self) -> None:
        self.x = 0
    
a = A()
print(hasattr(a,'x'))
print(hasattr(a,'y'))
