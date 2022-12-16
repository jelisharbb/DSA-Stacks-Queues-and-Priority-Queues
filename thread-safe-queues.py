# this program implements the classic multi-producer, multi-consumer problem using Python’s thread-safe queues

# import modules
import argparse, threading
from random import randint
from time import sleep

# import classes
from queue import LifoQueue, PriorityQueue, Queue

# store the imported classes in a dictionary
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}

# products that the producers will pick at random and pretend to be working on
PRODUCTS = (
    ":balloon:",
    ":cookie:",
    ":crystal_ball:",
    ":diving_mask:",
    ":flashlight:",
    ":gem:",
    ":gift:",
    ":kite:",
    ":party_popper:",
    ":postal_horn:",
    ":ribbon:",
    ":rocket:",
    ":shaved_ice:",
    ":shortcake:",
    ":teddy_bear:",
    ":thread:",
    ":umbrella_with_rain_drops:",
    ":unicorn_face:",
    ":violin:",
    ":volcano:",
    ":waning_crescent_moon:",
    ":water_wave:",
    ":yellow_heart:",
    ":yo-yo:",
    ":zombie:",
)

# the worker class extends the threading.Thread class and configures itself as a daemon thread so that its instances won’t prevent the program from exiting when the main thread finishes
class Worker(threading.Thread):
    def __init__(self, speed, buffer):
        super().__init__(daemon=True)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0

    @property
    # returns a string with either the product’s name and the progress of work or a generic message indicating that the worker is currently idle
    def state(self):
        if self.working:
            return f"{self.product} ({self.progress}%)"
        return ":zzz: Idle"

    # resets the state of a worker thread and goes to sleep for a few randomly chosen seconds
    def simulate_idle(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 3))

    # picks a random delay in seconds adjusted to the worker’s speed and progresses through the work
    def simulate_work(self):
        self.working = True
        self.progress = 0
        delay = randint(1, 1 + 15 // self.speed)
        for _ in range(100):
            sleep(delay / 100)
            self.progress += 1

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

