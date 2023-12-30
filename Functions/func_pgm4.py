# variable arguments
# A function can take any number of arguments

def sum(*x):
    s=0
    for i in x: s+= i
    print(s)


sum(2)  # 2
sum(2,3)  # 5
sum(2,3,4)  # 9
sum(2,3,4,5) # 14