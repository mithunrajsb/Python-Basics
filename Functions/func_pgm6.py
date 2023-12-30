# returning tuple from function
def calc(x,y):
    t=(x+y,x-y,x*y,x/y)
    return t

result = calc(5,6)
print(result)

print("Sum= ",result[0],"difference= ",result[1])