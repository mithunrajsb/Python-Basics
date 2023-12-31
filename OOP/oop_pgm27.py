# Empty classes 
# It is possible to start with an empty class but add 
# instance variables directly in the instances

class A: pass

a=A()
a.x = 10
a.y = 20

print(a.x)