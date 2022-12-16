# this program implements the classic multi-producer, multi-consumer problem using Python’s thread-safe queues

# import modules
import argparse, threading
from random import choice, randint
from time import sleep
from itertools import zip_longest
from dataclasses import dataclass, field
from enum import IntEnum

from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

# import classes
from queue import LifoQueue, PriorityQueue, Queue

# store the imported classes in a dictionary
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}

# class for a synchronized priority queue or a heap
@dataclass(order=True)
class Product:
    priority: int
    label: str = field(compare=False)

    def __str__(self):
        return self.label

class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

PRIORITIZED_PRODUCTS = (
    Product(Priority.HIGH, ":1st_place_medal:"),
    Product(Priority.MEDIUM, ":2nd_place_medal:"),
    Product(Priority.LOW, ":3rd_place_medal:"),
)

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

# this class works in an infinite loop, choosing a random product and simulating some work before putting that product onto the queue, called a buffer. it then goes to sleep for a random period, and when it wakes up again, the process repeats.
class Producer(Worker):
    def __init__(self, speed, buffer, products):
        super().__init__(speed, buffer)
        self.products = products

    # loop for producing products
    def run(self):
        while True:
            self.product = choice(self.products)
            self.simulate_work()
            self.buffer.put(self.product)
            self.simulate_idle()

# this class also works in an infinite loop, waiting for a product to appear in the queue
class Consumer(Worker):
    def run(self):
        while True:
            self.product = self.buffer.get() # .get() method keep the consumer thread stopped and waiting until there’s at least one product in the queue
            self.simulate_work()
            self.buffer.task_done()
            self.simulate_idle()

# for displaying the overall processes of the queue
class View:
    def __init__(self, buffer, producers, consumers):
        self.buffer = buffer
        self.producers = producers
        self.consumers = consumers

    # function that animates the acting products (emojis)
    def animate(self):
        with Live(
            self.render(), screen=True, refresh_per_second=10
        ) as live:
            while True:
                live.update(self.render())

    # function for
    def render(self):

        # condition statement that will display the type of queue that the user chose
        match self.buffer:
            case PriorityQueue():
                title = "Priority Queue"
                products = map(str, reversed(list(self.buffer.queue)))
            case LifoQueue():
                title = "Stack"
                products = list(self.buffer.queue)
            case Queue():
                title = "Queue"
                products = reversed(list(self.buffer.queue))
            case _:
                title = products = ""

        # for displaying the above row, and panels below
        rows = [Panel(f"[bold]{title}:[/] {', '.join(products)}", width=82)]
        pairs = zip_longest(self.producers, self.consumers)
        for i, (producer, consumer) in enumerate(pairs, 1):
            left_panel = self.panel(producer, f"Producer {i}")
            right_panel = self.panel(consumer, f"Consumer {i}")
            rows.append(Columns([left_panel, right_panel], width=40))
        return Group(*rows)

    # for padding and alignment of the worker's progress
    def panel(self, worker, title):
        if worker is None:
            return ""
        padding = " " * int(29 / 100 * worker.progress)
        align = Align(
            padding + worker.state, align="left", vertical="middle"
        )
        return Panel(align, height=5, title=title)

# this function is the entry point, which receives the parsed arguments supplied by parse_args()
def main(args):
    buffer = QUEUE_TYPES[args.queue]()

    # producers thread
    producers = [
        Producer(args.producer_speed, buffer, PRODUCTS)
        for _ in range(args.producers)
    ]
    # consumers thread
    consumers = [
        Consumer(args.consumer_speed, buffer) for _ in range(args.consumers)
    ]

    for producer in producers: # loop to launch the producer
        producer.start()
    for consumer in consumers: # loop to launch the consumer
        consumer.start()

    view = View(buffer, producers, consumers)
    view.animate() # to display and animate the processes

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

# command for running and customizing the queue
# python thread-safe-queues.py --producers 3  --consumers 2  --producer-speed 2  --consumer-speed 2  --queue fifo