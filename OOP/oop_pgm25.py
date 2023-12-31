# Magic functions

# 1. Constructor & Destructor

class A:
    def __init__(self): print("Created")
    def __del__(self): print("Destroyed")

a = A()
del(a)