# Operator overloading

class A:
    def __add__(self,x):pass
o = A()
i=10
o+i  

i+o  # TypeError: unsupported operand type(s) for +: 'int' and 'A'