# generating a matrix (3*4)

M = [[1 for j in range(4)] for i in range(3)]
print(M)

M1 = [[i+1 for j in range(4)] for i in range(3)]
print(M1)

M2 = [[j+1 for j in range(4)] for i in range(3)]
print(M2)

M3 = [[4*i+j+1 for j in range(4)] for i in range(3)]
print(M3)