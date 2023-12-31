# Displaying the first 10 & last 10 lines of a file 
fileName = "factorials.txt"
start = 

try:
    file=open(fileName)
    lines = file.readlines()
    if len(lines)>10:lines = lines[-10:]
    print("".join(lines),end='')
    
except Exception as e:
    print("Unable to open file: {}".format(fileName))
    print("Reason: {}".format(str(e)))