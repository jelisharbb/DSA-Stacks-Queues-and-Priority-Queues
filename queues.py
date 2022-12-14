# modules to be used
from collections import deque
from heapq import heappop, heappush
from itertools import count

class IterableMixin:
    # for getting the length of elements
    def __len__(self):
        return len(self._elements)

    # loop for dequeuing elements 
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(IterableMixin):
    # for initializing/preparing the deque
    def __init__(self, *elements):
        self._elements = deque(elements)

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

class PriorityQueue(IterableMixin):
    # defined a heap elements using list
    def __init__(self):
        self._elements = []
        self._counter = count()

    # method to enqueue elements based on their priority using heappush
    def enqueueWithPriority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    # method to dequeue elements using heappop
    def dequeue(self):
        return heappop(self._elements)[-1]