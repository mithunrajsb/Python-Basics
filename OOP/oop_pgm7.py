# Constructors and Destructors

class A:
    def __init__(self) -> None:
        print("constructor")
    
    def __del__(self) -> None:
        print("Destructor")
    

a=A()
b=A()

del a  
del b 