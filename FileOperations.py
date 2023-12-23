f = open('Test.txt','w')
f.write('Apple\n')
f.write('Orange\n')
f.write('Grapes\n')
f.write('Pear\n')
f.close()

f1 = open('Test.txt','r')
print(f1.readline())
print(f1.readlines())
f1.close()

f = open('Test.txt','r')
line = f.readline()
while line:
    line = line.rstrip()
    print (line)
    line = f.readline()
