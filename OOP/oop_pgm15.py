# Inheritance demo
# Multiple inheritance

class A:
    def fa(self):
        print("A called")


class B:
    def fb(self):
        print("B called")


class C(A,B):
    def fc(self):
        self.fa()
        self.fb()
        print("C called")


c = C()
c.fc()