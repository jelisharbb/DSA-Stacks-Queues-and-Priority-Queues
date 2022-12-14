# module to be used
from typing import NamedTuple
import networkx as nx

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
            year = int(attrs["years"]) or None,
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