# Raising exceptions

try:
    n=int(input("Enter an integer :"))
    if n>100: raise ValueError()
    result = int(100/n)
    print("100/{} = {}".format(n, result))

except ValueError:
    print("Please enter an integer less than 100!")

except ZeroDivisionError:
    print("Sorry! Division by zero is not permitted!")

print("Thanks for using this program")