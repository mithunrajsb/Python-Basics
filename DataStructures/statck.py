# Stack is implemented using lists

S=[]   # Creation of stack
S.append(10)  # Push 10
S.append(50)  # Push 50
S.append(100) # Push 100

print(S)  # Display the content of stack

print(S.pop())  # Pop 100

print(S)

print(S[-1])  #Peek

print(len(S))  # Stack Size
print(len(S) == 0)  #Checking if the stack is empty?
