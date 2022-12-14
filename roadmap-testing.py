# # module to be used
# import networkx as nx

# # read and print the roadmap.dot file
# print(nx.nx_agraph.read_dot("roadmap.dot"))

# -------------------------------------------

# # access print the details in the node london
# graph = nx.nx_agraph.read_dot("roadmap.dot")
# print(graph.nodes["london"])

# -------------------------------------------

# imported the class and class method from graph.py
from graph import City, load_graph

# call the load_graph class method, stored it in variables, the displayed it
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print(nodes["london"])
print(graph)