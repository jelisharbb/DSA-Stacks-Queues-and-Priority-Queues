# get the PriorityQueue class from queues.py
from queues import PriorityQueue

# define a priority value
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()

# enqueue elements
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# dequeue elements based on their priority
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())