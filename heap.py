# modules to be used
from heapq import heappush
from heapq import heappop

fruits = []

# adding elements
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

# resulting elements will not be sorted
print(fruits)

# remove and display elements
print(heappop(fruits)) # you'll get the first element from the heap
print(heappop(fruits)) # you'll get random elements
print(heappop(fruits)) # you'll get random elements