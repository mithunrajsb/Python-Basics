# Unpacking argument list

def calc(x,y):
    return (x+y,x-y,x*y,x/y)

L=[2,3]
print(calc(*L))

D = {'x':2,'y':3}
print(calc(**D))