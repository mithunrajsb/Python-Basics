x = int(input("Please enter an integer: "))

if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
else:
    print("Postive number")



# for loops
fruits = ['apple','banana','cherry','orange']
for fruit in fruits:
    print(fruit, len(fruit))