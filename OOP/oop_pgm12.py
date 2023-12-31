#Inheritance demo
# Function overriding demo 3,
# Invoking A's method without involving B's derived method.


class A:
    def fn(self):
        print("A.fn")


class B(A):
    def fn(self):
        print("B.fn")
        super().fn()


b = B()

A.fn(b)