L = [1,4,6,5,9,8,27]

def f(x):
    return x%2==0

M=list(filter(f,L))

print(M)
