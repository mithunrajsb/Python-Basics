# map() with multiple iterables

L1 = [1,2,3]
L2 = [4,5,6]
L3 = [7,8,9]

def f(a,b,c):
    return a+b+c

M = list(map(f,L1,L2,L3))

print(L1)
print(L2)
print(L3)
print(M)
