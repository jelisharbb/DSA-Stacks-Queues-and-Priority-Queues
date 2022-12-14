# get the Queue class from queues.py
from queues import Queue

fifo = Queue()

# add element
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

# remove and print element
print()
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())


# another way of adding elements
fifo = Queue("1st", "2nd", "3rd")
print(f"\nNumber of elements: {len(fifo)}")

# printing all elements
for elements in fifo:
    print(elements)

print(f"Updated number of elements: {len(fifo)}\n")