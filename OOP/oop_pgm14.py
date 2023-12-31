#Inheritance demo
# Function overriding demo 5,
# Order of constructors and destructors function call


class A:
    def __init__(self) -> None:
        print("A constructed")
    def __del__(self):
        print("A destroyed")
    def fn(self):
        print("A.fn")


class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("B constructed")
    def __del__(self):
        print("B destroyed")
        super().__del__()
    def fn(self):
        print("B.fn")
        super().fn()


b = B()
del(B)