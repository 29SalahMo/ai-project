"""
AI Project - Interactive Main Menu
This script provides an interactive interface to run different AI algorithms.
"""

import sys
from uniform_cost_search import uniform_cost_search, get_default_graph
from greedy_search import greedy_search, get_default_graph as get_greedy_graph, get_default_heuristic
from decision_tree_classifier import run_decision_tree

def print_separator():
    """Print a visual separator line."""
    print("=" * 60)

def print_menu():
    """Display the main menu options."""
    print_separator()
    print("           AI PROJECT - INTERACTIVE MENU")
    print_separator()
    print("1. Uniform Cost Search Algorithm")
    print("2. Greedy Search Algorithm")
    print("3. Decision Tree Classifier (Iris Dataset)")
    print("4. Exit")
    print_separator()

def run_uniform_cost_search():
    """Run Uniform Cost Search with user interaction."""
    print("\n--- Uniform Cost Search ---")
    print("\nDefault graph structure:")
    graph = get_default_graph()
    print_graph(graph)
    
    print("\nOptions:")
    print("1. Use default graph")
    print("2. Enter custom graph")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "2":
        graph = get_custom_graph()
        if not graph:
            print("Invalid graph input. Using default graph.")
            graph = get_default_graph()
    
    print("\nAvailable nodes:", list(graph.keys()))
    start = input("Enter start node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()
    
    if start not in graph or goal not in graph:
        print("Error: Invalid node names!")
        return
    
    print(f"\nSearching for path from {start} to {goal}...")
    result, visited = uniform_cost_search(graph, start, goal)
    
    if result:
        print(f"\n✓ Path found: {' -> '.join(result)}")
        print(f"Total cost: {calculate_path_cost(graph, result)}")
        print(f"Visited nodes: {sorted(visited)}")
    else:
        print("\n✗ Goal state not reachable.")
        print(f"Visited nodes: {sorted(visited)}")

def run_greedy_search():
    """Run Greedy Search with user interaction."""
    print("\n--- Greedy Search Algorithm ---")
    print("\nDefault graph structure:")
    graph = get_greedy_graph()
    print_graph(graph)
    
    print("\nOptions:")
    print("1. Use default graph")
    print("2. Enter custom graph")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "2":
        graph = get_custom_graph()
        if not graph:
            print("Invalid graph input. Using default graph.")
            graph = get_greedy_graph()
    
    print("\nAvailable nodes:", list(graph.keys()))
    start = input("Enter start node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()
    
    if start not in graph or goal not in graph:
        print("Error: Invalid node names!")
        return
    
    heuristic = get_default_heuristic()
    print(f"\nSearching for path from {start} to {goal} using Greedy Search...")
    result, visited = greedy_search(graph, start, goal, heuristic)
    
    if result:
        print(f"\n✓ Path found: {' -> '.join(result)}")
        print(f"Visited nodes: {sorted(visited)}")
    else:
        print("\n✗ Goal state not reachable.")
        print(f"Visited nodes: {sorted(visited)}")

def run_decision_tree():
    """Run Decision Tree Classifier."""
    print("\n--- Decision Tree Classifier ---")
    print("Running Decision Tree Classifier on Iris Dataset...")
    print("This will train a model to classify iris flowers.\n")
    run_decision_tree()

def print_graph(graph):
    """Print graph structure in a readable format."""
    for node, neighbors in graph.items():
        neighbor_str = ", ".join([f"{n}({cost})" for n, cost in neighbors.items()])
        print(f"  {node}: {neighbor_str}")

def get_custom_graph():
    """Get custom graph from user input."""
    print("\nEnter graph structure (format: Node1:Node2:cost,Node3:cost; ...)")
    print("Example: A:B:1,C:4; B:A:1,C:2,D:5; C:A:4,B:2,D:1; D:B:5,C:1")
    graph_input = input("Graph: ").strip()
    
    try:
        graph = {}
        edges = graph_input.split(';')
        for edge_group in edges:
            edge_group = edge_group.strip()
            if not edge_group:
                continue
            parts = edge_group.split(':')
            if len(parts) < 2:
                continue
            node = parts[0].strip().upper()
            graph[node] = {}
            
            # Parse neighbors
            neighbors_str = ':'.join(parts[1:])
            neighbor_pairs = neighbors_str.split(',')
            for pair in neighbor_pairs:
                pair = pair.strip()
                if ':' in pair:
                    neighbor, cost = pair.rsplit(':', 1)
                    graph[node][neighbor.strip().upper()] = float(cost.strip())
        
        # Ensure bidirectional edges
        for node in graph:
            for neighbor, cost in graph[node].items():
                if neighbor not in graph:
                    graph[neighbor] = {}
                if node not in graph[neighbor]:
                    graph[neighbor][node] = cost
        
        return graph if graph else None
    except Exception as e:
        print(f"Error parsing graph: {e}")
        return None

def calculate_path_cost(graph, path):
    """Calculate total cost of a path."""
    total = 0
    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]]
    return total

def main():
    """Main interactive loop."""
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            run_uniform_cost_search()
        elif choice == "2":
            run_greedy_search()
        elif choice == "3":
            run_decision_tree()
        elif choice == "4":
            print("\nThank you for using AI Project! Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")
        
        input("\nPress Enter to continue...")
        print()

if __name__ == "__main__":
    main()
