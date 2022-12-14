# get the Stack class from queues.py
from queues import Stack

# add elements to the stack
lifo = Stack("1st", "2nd", "3rd")

# remove elements from the stack
for element in lifo:
    print(element)


# another way
lifo = []

# add elements to the stack
lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

# remove elements from the stack
print()
print(lifo.pop())
print(lifo.pop())
print(lifo.pop())