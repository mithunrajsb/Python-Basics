#Inheritance demo
# Function overriding demo 2, calling base class method


class A:
    def fn(self):
        print("A.fn")


class B(A):
    def fn(self):
        print("B.fn")
        super().fn()


b = B()
b.fn()