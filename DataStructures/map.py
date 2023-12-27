def multTwo(x):
    return 2*x


L = [1,2,4,8,16]
M = list(map(multTwo,L))

print(L)
print(M)


def f(x):
    return x.upper()

L = ["Hello", "World"]
M = list(map(f,L))

print(L)
print(M)
