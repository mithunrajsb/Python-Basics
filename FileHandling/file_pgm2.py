from math import factorial

try:
    fileName = "factorials.txt"
    file = open(fileName,"w")
    for i in range(1,11):
        file.write("The factorial of {} is {}\n".format(i,factorial(i)))

except Exception as e:
    print("Unable to open the file {}".format(fileName))
    print("Reason: {}".format(str(e)))
else:
    print("Output successfully written to the file {}".format(fileName))