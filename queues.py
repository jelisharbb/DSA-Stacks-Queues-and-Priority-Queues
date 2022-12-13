from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    # for adding element
    def enqueue(self, element):
        self._elements.append(element)

    # for removing element
    def dequeue(self):
        return self._elements.popleft()
