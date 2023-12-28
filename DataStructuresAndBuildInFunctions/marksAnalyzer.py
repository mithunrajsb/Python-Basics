#Program to analyze the marks of N students in a class

# This program uses map(), filter() and reduce()

from functools import reduce

marks = list(map(lambda x: int(x),input("Enter the marks of 'n' students: ").split(' ')))
n = len(marks)
#int x
maxMarks = max(marks)
minMarks = min(marks)

sumMarks = reduce(lambda x,y:x+y, marks)
avgMarks = sumMarks/n

numPasses = len(list(filter(lambda x: x> 35, marks)))
numFailures = n-numPasses
percentPasses = numPasses/n * 100

print("Analyzed marks on {} students:" .format(n))
print("Minimum marks: {} Maximum marks : {}" .format(minMarks, maxMarks))
print("Average Marks: {}" .format(avgMarks))
print("Passes: {} Failures: {} " .format(numPasses,numFailures))
print("Pass Percentage: {}" .format(percentPasses))

