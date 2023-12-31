#Inheritance demo
# Function overriding demo


class A:
    def fn(self):
        print("A.fn")


class B(A):
    def fn(self):
        print("B.fn")


b = B()
b.fn()