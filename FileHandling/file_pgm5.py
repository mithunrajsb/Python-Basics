# Displaying the first 10 lines of a file using head command
fileName = "factorials.txt"

try:
    file=open(fileName)
    for i in range(20):
        data = file.readline()
        if not data: break
        print(data, end='')
except Exception as e:
    print("Unable to open file: {}".format(fileName))
    print("Reason: {}".format(str(e)))