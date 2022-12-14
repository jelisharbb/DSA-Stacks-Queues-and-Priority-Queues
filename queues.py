# modules to be used
from collections import deque
from heapq import heappop, heappush

class Queue:
    # for initializing/preparing the deque
    def __init__(self, *elements):
        self._elements = deque(elements)

    # for getting the length of deque
    def __len__(self):
        return len(self._elements)

    # loop for dequeuing elements 
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    # for adding element
    def enqueue(self, element):
        self._elements.append(element)

    # for removing element
    def dequeue(self):
        return self._elements.popleft()

# defined Stack class then inherited the Queue class
class Stack(Queue):
    # override the dequeue method
    def dequeue(self):
        return self._elements.pop()

class PriorityQueue:
    # defined a heap elements using list
    def __init__(self):
        self._elements = []

    # method to enqueue elements based on their priority using heappush
    def enqueueWithPriority(self, priority, value):
        heappush(self._elements, (priority, value))

    # method to dequeue elements using heappop
    def dequeue(self):
        return heappop(self._elements)