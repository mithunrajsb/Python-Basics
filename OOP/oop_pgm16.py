# Inheritance demo
# Multiple inheritance - function overriding

class A:
    def fn(self):
        print("A")


class B:
    def fn(self):
        print("B")


class C(A,B):
    def fn(self):
        print("C")


c = C()
c.fn()