# module, and class to be used
from typing import NamedTuple
import networkx as nx
from queues import Queue

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
    for node in breadth_first_traverse(graph, source,  order_by):
        if predicate(node):
            return node

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