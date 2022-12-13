from collections import deque

class Queue:
    # 
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
