# Writing to binary file

import pickle

class Employee:
    def __init__(self,name,id,designation): 
        self.name = name
        self.id = id
        self.designation = designation


try:
    file = open("employee.dat","ab")
    name = input("Enter employee name:")
    id = int(input("Enter employee ID:"))
    designation = input("Enter employee designation:")
    pickle.dump(Employee(name,id,designation),file)

except Exception as e:
    print("Unable to open the file!")
    print("Reason: {}".format(str(e)))
else:
    print("Employee record successfully written to the file")