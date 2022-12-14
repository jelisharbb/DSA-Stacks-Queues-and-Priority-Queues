# get the PriorityQueue class from queues.py
from queues import PriorityQueue

# define a priority value
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()

# enqueue elements
messages.enqueueWithPriority(IMPORTANT, "Windshield wipers turned on")
messages.enqueueWithPriority(NEUTRAL, "Radio station tuned in")
messages.enqueueWithPriority(CRITICAL, "Brake pedal depressed")
messages.enqueueWithPriority(IMPORTANT, "Hazard lights turned on")

# dequeue elements based on their priority
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())