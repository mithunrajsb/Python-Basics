def sum(x,y):
    return x+ y


# Default arguments
def sum_numbers(a,b,c=30,d=40):
    return a + b + c + d


print(sum(5,6))

print(sum_numbers(10,20))  # 100
print(sum_numbers(10,20,10))  # 80
print(sum_numbers(10,20,10,20)) # 60
print(sum_numbers(10))  # print(sum_numbers(10))
                        #          ^^^^^^^^^^^^^^^
                        # TypeError: sum_numbers() missing 1 required positional argument: 'b'
