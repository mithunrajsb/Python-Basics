# Class functions

class A:
    x=10
    def increment(self):
        A.x = A.x + 1
    
    def increment_self(self):
        self.x = self.x + 10


print(A.x)

a = A()
print(a.x)
a.increment()
print(a.x)
print(A.x)

a.increment_self()
print(a.x)
print(A.x)