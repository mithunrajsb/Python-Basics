#Class variables

class A:
    x = 10

print(A.x)

a = A()
b=A()

print(a.x)
print(b.x)

a.x = 50
print(a.x)
print(b.x)