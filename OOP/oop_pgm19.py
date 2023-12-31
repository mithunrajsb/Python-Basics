# Inheritance

# Dynamic polymorphism demo

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")
    def speak(self):
        print("Bow Bow..")

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")
    def speak(self):
        print("Meow!")


def introduce(animal):
    print("Hi! This animal is called ",animal.name)
    print("This animal says: ", end=' ')
    animal.speak()

animal1 = Dog()
introduce(animal1)

animal2 = Cat()
introduce(animal2)