# module to be used
import networkx as nx

# read and print the roadmap.dot file
print(nx.nx_agraph.read_dot("roadmap.dot"))

# access print the details in the node london
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])