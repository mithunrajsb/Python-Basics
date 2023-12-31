# standard attributes

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        pass


print("__name__:",Animal.__name__)
print("__doc__:",Animal.__doc__)
print("__bases__:",Animal.__bases__)
print("__module__:",Animal.__module__)
print("__dict__:",Animal.__dict__)
