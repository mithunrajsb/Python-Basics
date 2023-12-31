#Inheritance demo
# Function overriding demo 5,
# Order of constructors and destructors function call


class A:
    def __init__(self) -> None:
        print("A constructed")
    def __del__(self):
        print("A destroyed")
    

class B:
    def __init__(self) -> None:
        print("B constructed")
    def __del__(self):
        print("B destroyed")
   

class C(A,B):
    def __init__(self) -> None:
        A.__init__(self)
        B.__init__(self)
        print("C constructed")
    def __del__(self):
        print("C destroyed")
        B.__del__(self)
        A.__del__(self)
   


c = C()
del(c)