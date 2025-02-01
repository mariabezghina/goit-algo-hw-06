import networkx as nx

G = nx.Graph()

stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
G.add_nodes_from(stations)

edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E'),
         ('E', 'F'), ('F', 'G'), ('B', 'D'), ('C', 'F')]
G.add_edges_from(edges)

def dfs(graph, start):
    visited = set()
    path = []
    
    def dfs_recursive(node):
        visited.add(node)
        path.append(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    dfs_recursive(start)
    return path

def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            path.append(node)
            queue.extend(neighbor for neighbor in graph.neighbors(node) if neighbor not in visited)
    
    return path

start_node = 'A'
dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print(f"DFS path starting from {start_node}: {dfs_path}")
print(f"BFS path starting from {start_node}: {bfs_path}")
