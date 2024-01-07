# If we list all the natural numbers below 10 that are multiples of 3 or 5
# we get 3, 5, 6  and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000


def findSum(mult1,mult2,limit):
    n, total = 1,0
    while n<limit:
        if n%mult1 == 0 or n%mult2 == 0:
            total += n
        n+=1
    return total

print("Multiples of 3 or 5 below 10: ",findSum(3,5,10))
print("Multiples of 3 or 5 below 100: ",findSum(3,5,100))
print("Multiples of 3 or 5 below 1000: ",findSum(3,5,1000))
