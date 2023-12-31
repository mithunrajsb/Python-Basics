# Reading from binary file

import pickle

class Employee:
    def __init__(self,name,id,designation): 
        self.name = name
        self.id = id
        self.designation = designation


try:
    file = open("employee.dat","rb")
    while 1:
        emp = pickle.load(file)
        print("Name : {} ID: {} Designation: {}".format(emp.name,emp.id,emp.designation))

except EOFError: pass

except Exception as e:
    print("Unable to open the file!")
    print("Reason: {}".format(str(e)))
