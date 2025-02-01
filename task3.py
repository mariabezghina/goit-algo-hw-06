import networkx as nx

G_weighted = nx.Graph()

stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
G_weighted.add_nodes_from(stations)

edges_weighted = [('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 5), ('C', 'D', 10),
                  ('D', 'E', 3), ('E', 'F', 7), ('F', 'G', 6), ('B', 'D', 3), ('C', 'F', 1)]
G_weighted.add_weighted_edges_from(edges_weighted)

def dijkstra(graph, start):
    lengths, paths = nx.single_source_dijkstra(graph, start)
    return lengths, paths

start_node = 'A'

distances, paths = dijkstra(G_weighted, start_node)

print(f"Shortest paths from {start_node}:")
for target, path in paths.items():
    print(f"To {target}: {path} with distance {distances[target]}")
