# this program implements the classic multi-producer, multi-consumer problem using Python’s thread-safe queues

# import modules and classes
import argparse
from queue import LifoQueue, PriorityQueue, Queue

# store the imported classes in a dictionary
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}

# this function is the entry point, which receives the parsed arguments supplied by parse_args()
def main(args):
    buffer = QUEUE_TYPES[args.queue]()

# this function defines and add the default value for the queues
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--queue", choices=QUEUE_TYPES, default="fifo")
    parser.add_argument("-p", "--producers", type=int, default=3)
    parser.add_argument("-c", "--consumers", type=int, default=2)
    parser.add_argument("-ps", "--producer-speed", type=int, default=1)
    parser.add_argument("-cs", "--consumer-speed", type=int, default=1)
    return parser.parse_args()

# this statement is a way to store code that should only run when your file is executed as a script
if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        pass