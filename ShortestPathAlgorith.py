INF = float('inf') # Used to indicate inifinite distance between two nodes
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0]
    ]

# if no target node is specified, the function should compute the shortest paths from the starting node to all other nodes in the graph
def shortest_path(matrix, start_node, target_node = None): 
    n = len(matrix) # Store number of nodes in the graph
    
    distances = [INF] * n # Keep track of the shortest known distance from the start node
    distances[start_node] = 0 # Distance from start node to itself
    
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n
    
    for _ in range(n):
        min_distance = INF
        current = -1
        
        for node_no in range(n): # check every node to find the one with the smallest known distance
            if not visited[node_no] and distances[node_no] < min_distance: # If true then the current node is the best unvisited option so far
                min_distance = distances[node_no]
                current = node_no
        
        if current == -1:
            break
        
        visited[current] = True
        
        # Distance from current node to the neighbor node
        for node_no in range(n):
            distance = matrix[current][node_no]
            
            # Calulating possible distance to the neighbor
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]
    
    targets = [target_node] if target_node is not None else range(n)
    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue
        string_path = (str(n) for n in paths[node_no]) # Generator expression
        path = ' -> '.join(string_path)
        
        print(f"\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}")
    
    return distances, paths

# --> Example Usage <--
shortest_path(adj_matrix, 0, 5)
shortest_path(adj_matrix, 0, 4)
shortest_path(adj_matrix, 0, 2)
shortest_path(adj_matrix, 0, 3)
shortest_path(adj_matrix, 0, 1)