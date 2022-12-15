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

# this allows you to update the element priorities as you discover cheaper connections
## this specialized priority queue stores data class elements instead of tuples because the elements must be mutable
### also, this lets you peek or modify the priority of an element using the square bracket syntax
@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value