#Inheritance demo
# Private, Public and Protected

class A:
    def __f1(self): print("A.f1")   #private method
    def f2(self):print("A.f2")     # public method
    def _f3(self):print("A.f3")   #protected method

class B(A):
    def __g1(self):print("B.g1")
    def g2(self):print("B.g2")
    def _g3(self):print("B.g3")

b=B()

b.f2()
#b.__f1()
b._f3()
b.g2()
#b.__g1()
b._g3()

a = A()
#a.__f1()
a.f2()
a._f3()