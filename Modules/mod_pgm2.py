import fact
def ncr(n,r):
    return int(fact.factorial(n) / (fact.factorial(r) * fact.factorial(n-r)))

x,y = input("Enter 2 Integers:").split(' ')
x,y = int(x), int(y)
print("The combination of {} and {} is {}".format(x,y,ncr(x,y)))