# Queue can be implemented using collections.deque

from collections import deque

q = deque()   # Creationf of a queue
q.append(10)  # Insert 10
q.append(20)  # Insert 20
q.append(30)  # Insert 30
print(q)      # Display the queue

print(q.popleft())  # Delete 10
print(q)            # Display the queue
print(q.pop())         # Delete 30

print(len(q))   # Queue size
print(q)
print(len(q) == 0)  # Queue empty?
