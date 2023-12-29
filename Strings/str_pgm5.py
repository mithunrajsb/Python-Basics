# ljust and rjust

s="Hello"
print(s)

print(s.ljust(20))

print(s.ljust(2))

print(s.ljust(20,"="))

print(s.ljust(2,"="))


print(s.rjust(20))
print(s.rjust(20,'-'))
print(s.rjust(2))
print(s.rjust(2,'-'))


print(s.center(20))
print(s.center(2))
print(s.center(20,"="))
print(s.center(2,"="))