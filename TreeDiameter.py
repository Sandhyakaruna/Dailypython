from collections import deque, defaultdict

def bfs_farthest(node, graph, n):
    dist = [-1] * (n + 1)
    dist[node] = 0
    queue = deque([node])
    farthest_node = node
    max_dist = 0

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
                if dist[v] > max_dist:
                    max_dist = dist[v]
                    farthest_node = v
    return farthest_node, max_dist

def tree_diameter(graph, n):
  
    node, _ = bfs_farthest(1, graph, n)
    # Find the diameter from the farthest node found
    _, diameter = bfs_farthest(node, graph, n)
    return diameter

def maxDiameter(N, edges1, M, edges2):
    # Build graph for the first tree
    graph1 = defaultdict(list)
    for u, v in edges1:
        graph1[u].append(v)
        graph1[v].append(u)
    
    # Build graph for the second tree
    graph2 = defaultdict(list)
    for u, v in edges2:
        graph2[u].append(v)
        graph2[v].append(u)
    
    # Compute diameters of both trees
    diameter1 = tree_diameter(graph1, N)
    diameter2 = tree_diameter(graph2, M)
    
    # The maximum possible diameter is:
    max_diameter = diameter1 + diameter2 + 1
    
    # BFS to find the distance from all nodes in tree1 to all nodes in tree2
    def bfs_all_distances(graph, start_node, n):
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = deque([start_node])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        return distances
    
    # Get distances from farthest nodes
    farthest_from_tree1 = bfs_farthest(1, graph1, N)[0]
    distances_from_tree1 = bfs_all_distances(graph1, farthest_from_tree1, N)
    
    farthest_from_tree2 = bfs_farthest(1, graph2, M)[0]
    distances_from_tree2 = bfs_all_distances(graph2, farthest_from_tree2, M)
    
    # Find how many ways to achieve maximum diameter
    count = 0
    for i in range(1, N + 1):
        for j in range(N + 1, N + M + 1):
            if distances_from_tree1[i] + distances_from_tree2[j - N] == max_diameter - 1:
                count += 1
    
    return count

# Example usage:
N = 4
edges1 = [(1, 2), (2, 3), (3, 4)]
M = 3
edges2 = [(5, 6), (6, 7)]
print(maxDiameter(N, edges1, M, edges2))  # Output: 4
