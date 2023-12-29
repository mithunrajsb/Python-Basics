import math

angle = float(input("Enter an angle in degrees: "))
angle = math.radians(angle)

print("sin(x) = ",round(math.sin(angle),2))
print("cos(x) = ",round(math.cos(angle),2))
print("tan(x) = ",round(math.tan(angle),2))

print("cosec(x) = ",round(1/math.sin(angle),2))
print("sec(x) = ",round(1/math.cos(angle),2))
print("cot(x) = ",round(1/math.tan(angle),2))