# Magic functions

# 1. Constructor & Destructor

class A:
    def __init__(self): print("Created")
    def __del__(self): print("Destroyed")

a = A()
del(a)

# 2. Stringification
a1 = A()
print(str(a1))  # <__main__.A object at 0x10091b2d0>