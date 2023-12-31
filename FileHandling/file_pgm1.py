fileName = input("Enter a file name:")
try:
    file = open(fileName)
    contents = file.read()
    print(contents)

except Exception as e:
    print("Unable to open the file {}".format(fileName))
    print("Reason : {} ".format(str(e)))
