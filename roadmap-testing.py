# ----------------- test 1 --------------------------

# # module to be used
# import networkx as nx

# # read and print the roadmap.dot file
# print(nx.nx_agraph.read_dot("roadmap.dot"))

# # access print the details in the node london
# graph = nx.nx_agraph.read_dot("roadmap.dot")
# print(graph.nodes["london"])

# ----------------- test 2 --------------------------

# # imported the class and class method from graph.py
# from graph import City, load_graph

# # call the load_graph class method, stored the results in two variables, the displayed it
# nodes, graph = load_graph("roadmap.dot", City.from_dict) # node variable - obtain a reference to an instance of the City class by the specified name; graph variable - holds the entire networkx Graph object
# print(nodes["london"])
# print(graph)

# print(f"\nNeighbors:")
# # loop that identifies the immediate neighbors of the specified city using .neighbors() method
# for neighbor in graph.neighbors(nodes["london"]):
#     print(neighbor.name) 

# print(f"\nNeighbors together with their respective distances:")
# # loop that identifies the immediate neighbors of the specified city and their respective distances
# for neighbor, weights in graph[nodes["london"]].items():
#     print(weights["distance"], neighbor.name) # neighbors are always listed in the same order in which you defined them in the DOT file

# # function that returns the list of neighbors and their weights sorted by the specified strategy. the strategy takes a dictionary of all the weights associated with an edge and returns a sorting key
# def sort_by(neighbors, strategy):
#     return sorted(neighbors.items(), key = lambda item: strategy(item[1]))

# # function that produces a floating-point distance based on the input dictionary
# def by_distance(weights):
#     return float(weights["distance"])

# print(f"\nNeighbors sorted by their distances:")
# # loop that iterate over the neighbors of London, sorted by distance in ascending order
# for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
#     print(f"{weights['distance']:>3} miles, {neighbor.name}")

# --------- test 3: breadth-first search ------------

# modules, class, and class method to be used
import networkx as nx
from graph import City, load_graph

# defined a function that returns year within 20th century
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

# call the load_graph class method, then stored the results in two variables
nodes, graph = load_graph("roadmap.dot", City.from_dict)

print()
# loop that iterate over the neighbors of the specified city using breadth-first search
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print ("📍", node.name)
    # finds a city that has a year within the 20th century
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")

# function that sorts the city based on their latitude
def order(neighbors):
    # function that gets the latitude of the cities
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key = by_latitude, reverse = True))