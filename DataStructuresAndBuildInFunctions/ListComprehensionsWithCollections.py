c = [(x,x) for x in range(1,11)]

print(c)

sqList = [(x,x*x) for x in range(1,11)]
print(sqList)

#excluding the odd numbers from the above list
evenSqList = [(x,x*x) for x in range(1,11) if x%2==0 ]
print(evenSqList)

#multiple variables
coord = [(x,y,z) for x in range(1,4) for y in range(1,x) for z in range(1,y+1)]
print("multiple variables")
print(coord)