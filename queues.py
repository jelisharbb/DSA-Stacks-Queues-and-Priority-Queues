# modules to be used
from collections import deque
from dataclasses import dataclass
from heapq import heappop, heappush, heapify
from itertools import count
from typing import Any

class IterableMixin:
    # make the class compatible with the len() function
    def __len__(self):
        return len(self._elements)

    # make the class instances usable in a for loop. also, __iter__() causes your custom queue to reduce its size by dequeuing elements from itself as you iterate over it
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

# defined Queue class, then inherited the IterableMixin class
class Queue(IterableMixin):
    # for initializing/preparing the deque
    def __init__(self, *elements):
        self._elements = deque(elements) # leading underscore in the attribute’s name indicates an internal bit of implementation, which only the class should access and modify

    # for appending element
    def enqueue(self, element):
        self._elements.append(element)

    # for removing element
    def dequeue(self):
        return self._elements.popleft()

# defined Stack class, then inherited the Queue class
class Stack(Queue):
    # override the .dequeue() method from the Queue class to remove elements from the top of the stack
    def dequeue(self):
        return self._elements.pop()

# defined PriotityQueue class, then inherited the IterableMixin class
class PriorityQueue(IterableMixin):
    # defined a heap elements using list
    def __init__(self):
        self._elements = []
        self._counter = count() # this solves the sort instability. whenever you enqueue a value, the counter increments and retains its current state in a tuple pushed onto the heap

    # method to enqueue elements based on their priority using heappush
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value) # negate the priority to reverse the order
        heappush(self._elements, element)

    # method to dequeue elements using heappop
    def dequeue(self):
        return heappop(self._elements)[-1] # -1 index is used for accessing the last component the tuple

# defines the data type of the class attributes
@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

