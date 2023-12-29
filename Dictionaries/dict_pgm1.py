D = dict([('apple','red'),('grapes','green')])
print(D)

print(D['apple'])

# Iterating through all elements
for K, V in D.items():
    print(K,V)

# Checking for element
print('apple' in D)
print('Mango' in D)

# Using clear to delete all elements in a dictionary
D.clear()
print(D)