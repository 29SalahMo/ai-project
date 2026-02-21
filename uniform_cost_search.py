"""
Uniform Cost Search Algorithm
Finds the shortest path from start to goal using uniform cost search.
"""

import heapq

def uniform_cost_search(graph, start, goal):
    """
    Perform uniform cost search to find the shortest path.
    
    Args:
        graph: Dictionary representing the graph {node: {neighbor: cost}}
        start: Starting node
        goal: Goal node
    
    Returns:
        tuple: (path, visited_nodes) or (None, visited_nodes) if no path found
    """
    frontier = [(0, start, [])]
    visited = set()

    while frontier:
        cost, current, path = heapq.heappop(frontier)

        if current == goal:
            return path + [current], visited

        if current not in visited:
            visited.add(current)

            for neighbor, edge_cost in graph.get(current, {}).items():
                heapq.heappush(frontier, (cost + edge_cost, neighbor, path + [current]))

    return None, visited

def get_default_graph():
    """Return a default graph for demonstration."""
    return {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

if __name__ == "__main__":
    # Example usage
    graph = get_default_graph()
    start_node = 'A'
    goal_node = 'D'
    
    result, visited_cells = uniform_cost_search(graph, start_node, goal_node)
    
    if result:
        print("Uniform Cost Search Path:", result)
        print("Visited Cells:", sorted(visited_cells))
    else:
        print("Goal state not reachable.")
