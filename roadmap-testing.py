# ----------------- test 1 --------------------------

# # module to be used
# import networkx as nx

# # read and print the roadmap.dot file
# print(nx.nx_agraph.read_dot("roadmap.dot"))

# # access print the details in the node london
# graph = nx.nx_agraph.read_dot("roadmap.dot")
# print(graph.nodes["london"])

# ----------------- test 2 --------------------------

# imported the class and class method from graph.py
from graph import City, load_graph

# call the load_graph class method, stored the results in two variables, the displayed it
nodes, graph = load_graph("roadmap.dot", City.from_dict) # node variable - obtain a reference to an instance of the City class by the specified name; graph variable - holds the entire networkx Graph object
print(nodes["london"])
print(graph)

print(f"\nNeighbors:")
# identifies the immediate neighbors of the specified city using .neighbors() method
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)