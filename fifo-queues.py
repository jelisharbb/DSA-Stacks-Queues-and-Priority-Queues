from queues import Queue

fifo = Queue()

# add element
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

# remove and print element
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())


# another way 
fifo = Queue("1st", "2nd", "3rd")
print()
print(f"Number of elements: {len(fifo)}")