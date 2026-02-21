"""
Greedy Search Algorithm
Finds a path from start to goal using greedy best-first search with a heuristic.
"""

def greedy_search(graph, start, goal, heuristic):
    """
    Perform greedy search to find a path from start to goal.
    
    Args:
        graph: Dictionary representing the graph {node: {neighbor: cost}}
        start: Starting node
        goal: Goal node
        heuristic: Function that takes (node, goal) and returns heuristic value
    
    Returns:
        tuple: (path, visited_nodes) or (None, visited_nodes) if no path found
    """
    current = start
    path = [current]
    visited = set([current])

    while current != goal:
        neighbors = list(graph.get(current, {}).keys())

        if not neighbors:
            return None, visited  # Goal state not reachable

        # Find neighbor with minimum heuristic value
        next_node = min(neighbors, key=lambda neighbor: heuristic(neighbor, goal))
        
        # Check for cycles
        if next_node in visited:
            return None, visited
        
        path.append(next_node)
        visited.add(next_node)
        current = next_node

    return path, visited

def get_default_heuristic():
    """
    Return default heuristic function.
    Uses alphabetical distance as a simple heuristic.
    """
    return lambda node, goal: abs(ord(node) - ord(goal))

def get_default_graph():
    """Return a default graph for demonstration."""
    return {
        'A': {'B': 3, 'C': 5},
        'B': {'A': 3, 'D': 2},
        'C': {'A': 5, 'D': 6},
        'D': {'B': 2, 'C': 6}
    }

if __name__ == "__main__":
    # Example usage
    graph = get_default_graph()
    start_node = 'A'
    goal_node = 'D'
    
    heuristic = get_default_heuristic()
    result, visited = greedy_search(graph, start_node, goal_node, heuristic)
    
    if result:
        print("Greedy Search Path:", result)
        print("Visited Nodes:", sorted(visited))
    else:
        print("Goal state not reachable.")
