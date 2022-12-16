# module, and class to be used
from typing import NamedTuple
import networkx as nx
from queues import Queue, Stack, MutableMinHeap
from collections import deque
from math import inf as infinity

# defined a class that defines the data types of the following class attribute
class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    # defines a class method that takes a dictionary of attributes extracted from a DOT file and returns a new instance of the City class
    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name = attrs["xlabel"],
            country = attrs["country"],
            year = int(attrs["year"]) or None,
            latitude = float(attrs["latitude"]),
            longitude = float(attrs["longitude"]),
        )

# defined a function that gets the specific nodes and graph from the roadmap.dot file
def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename) # reads the DOT file
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data = True) 
    } # build a mapping of node identifiers to the object-oriented representation of the graph nodes

    return nodes, nx.Graph (
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data = True)
    ) # returns the mapping and a new graph comprising nodes and weighted edges\

# this function takes a networkx graph and the source node as arguments while yielding nodes visited with the breadth-first traversal
def breadth_first_traverse(graph, source, order_by =  None):
    queue = Queue(source)
    visited = {source}
    while queue:
        yield(node := queue.dequeue())
        neighbors = list(graph.neighbors(node))
        if order_by: # condition that allows sorting the neighbors in a particular order
            neighbors.sort(key = order_by)
        for neighbor in neighbors: # for loop that iterates over the neighbors
            if neighbor not in visited: # if statement to check unvisited neighboring cities, then add and enqueue them
                visited.add(neighbor)
                queue.enqueue(neighbor)

# this function builds on top of the first one by looping over the yielded nodes, and stops once the current node meets the expected criteria. if none of the nodes make the predicate truthy, then the function implicitly returns None
def breadth_first_search(graph, source, predicate, order_by =  None):
    return search(breadth_first_traverse, graph, source, predicate, order_by)

# this function takes another node as an argument and optionally lets you order the neighbors using a custom strategy
def shortest_path(graph, source, destination, order_by =  None):
    queue = Queue(source)
    visited = {source}
    previous = {} # stores the previous path taken
    while queue:
        node = queue.dequeue()
        neighbors = list(graph.neighbors(node))
        if order_by: # condition that allows sorting the neighbors in a particular order
            neighbors.sort(key = order_by)
        for neighbor in neighbors: # for loop that iterates over the neighbors
            if neighbor not in visited: # if statement to check unvisited neighboring cities, then add and enqueue them
                visited.add(neighbor)
                queue.enqueue(neighbor)
                previous[neighbor] = node
                if neighbor == destination:
                    return retrace(previous, source, destination)

# function that retrace the path from the destination to the starting point
def retrace(previous, source, destination):
    path = deque()

    current = destination
    while current != source:
        path.appendleft(current)
        current = previous.get(current)
        if current is None:
            return None

    path.appendleft(source)
    return list(path)

# this function tells whether two nodes remain connected or not
def connected(graph, source, destination):
    return shortest_path(graph, source, destination) is not None

# this function takes a networkx graph and the source node as arguments using depth-first traversal. this doesn't mark the source node as visited
def depth_first_traverse(graph, source, order_by=None):
    stack = Stack(source)
    visited = set() #  visited nodes are initialized in this set
    while stack:
        if (node := stack.dequeue()) not in visited:
            yield node
            visited.add(node)
            neighbors = list(graph.neighbors(node))
            if order_by: # condition that allows sorting the neighbors in a particular order
                neighbors.sort(key=order_by)
            for neighbor in reversed(neighbors): # for loop that iterates over the neighbors in reverse order, and enqueue them in the stack
                stack.enqueue(neighbor)

# by function, this avoid maintaining a stack of your own, as Python pushes each function call on a stack behind the scenes
def recursive_depth_first_traverse(graph, source, order_by=None):
    visited = set()

    def visit(node):
        yield node
        visited.add(node)
        neighbors = list(graph.neighbors(node))
        if order_by: # condition that allows sorting the neighbors in a particular order
            neighbors.sort(key=order_by)
        for neighbor in neighbors: # iterates over the neighbors
            if neighbor not in visited:
                yield from visit(neighbor)

    return visit(source)

# thi function loops over the yielded nodes, and stops once the current node meets the expected criteria
def depth_first_search(graph, source, predicate, order_by=None):
    return search(depth_first_traverse, graph, source, predicate, order_by)

# this function traverse with corresponding strategy
def search(traverse, graph, source, predicate, order_by=None):
    for node in traverse(graph, source, order_by):
        if predicate(node):
            return node

# 
def dijkstra_shortest_path(graph, source, destination, weight_factory):
    previous = {}
    visited = set()

    unvisited = MutableMinHeap()
    for node in graph.nodes:
        unvisited[node] = infinity
    unvisited[source] = 0