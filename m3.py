
import statistics
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = statistics.mean(speed)

print(x)

y = statistics.median(speed)
print(y)


z = statistics.mode(speed)
print(z)

sd = numpy.std(speed)
print(sd)


speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)
sd =  numpy.std(speed)

print(x)
print(sd)
y = numpy.sqrt(x)
print("sqrt of variance "+str(y))

