import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
G.add_nodes_from(stations)

edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E'), 
         ('E', 'F'), ('F', 'G'), ('B', 'D'), ('C', 'F')]
G.add_edges_from(edges)

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', edge_color='gray')
plt.title('Transport Network of the City')
plt.show()

num_nodes = G.number_of_nodes() 
num_edges = G.number_of_edges()
degree_sequence = [G.degree(node) for node in G.nodes()]

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Degree of each node: {degree_sequence}")
