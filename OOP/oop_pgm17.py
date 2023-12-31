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
        super().fn()  # base class function will be called based on the order of inheritance. Here A will be called
        print("C")


c = C()
c.fn()   