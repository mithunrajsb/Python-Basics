
def func1():
    print("This is from the function 1")

def func2():
    print("This is from the function 2")

def func3():
    print("This is from the function 3")

def func4(count):
    print("This is from the function 4")
    for i in range(count):
        print(i,end=", ")

def main():
    func1()
    func2()
    func3()
    func4(6)

if __name__ == "__main__":
    main()
