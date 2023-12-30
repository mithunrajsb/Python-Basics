# using global variable, setting global variable from a function

x = 2
def fn():
    global x
    x = 3
    print(x)

print(x)

fn()

print(x)