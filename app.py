"""
AI Project - Web Application
Streamlit web interface for AI algorithms
"""

import streamlit as st
import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from uniform_cost_search import uniform_cost_search, get_default_graph
from greedy_search import greedy_search, get_default_graph as get_greedy_graph, get_default_heuristic
from decision_tree_classifier import run_decision_tree_classifier

# Page configuration
st.set_page_config(
    page_title="AI Project - Search Algorithms & ML",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        padding: 1rem 0;
    }
    .algorithm-box {
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
    }
    .info-box {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #17a2b8;
    }
    </style>
""", unsafe_allow_html=True)

def display_graph(graph):
    """Display graph in a formatted way."""
    graph_str = ""
    for node, neighbors in graph.items():
        neighbor_str = ", ".join([f"**{n}** ({cost})" for n, cost in neighbors.items()])
        graph_str += f"- **{node}**: {neighbor_str}\n"
    return graph_str

def parse_custom_graph(graph_input):
    """Parse custom graph from user input."""
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
        st.error(f"Error parsing graph: {e}")
        return None

def calculate_path_cost(graph, path):
    """Calculate total cost of a path."""
    total = 0
    for i in range(len(path) - 1):
        total += graph[path[i]][path[i + 1]]
    return total

def main():
    """Main Streamlit application."""
    # Header
    st.markdown('<div class="main-header">🤖 AI Project - Search Algorithms & Machine Learning</div>', 
                unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar navigation
    st.sidebar.title("📋 Navigation")
    algorithm = st.sidebar.radio(
        "Choose an Algorithm:",
        ["🏠 Home", "🔍 Uniform Cost Search", "🎯 Greedy Search", "🌳 Decision Tree Classifier"]
    )
    
    # Home page
    if algorithm == "🏠 Home":
        st.markdown("""
        ## Welcome to AI Project! 👋
        
        This web application demonstrates various AI algorithms:
        
        ### 🔍 **Uniform Cost Search**
        - Finds the shortest path in a weighted graph
        - Guarantees optimal solution
        - Uses priority queue for efficient search
        
        ### 🎯 **Greedy Search**
        - Heuristic-based pathfinding algorithm
        - Fast but may not find optimal solution
        - Uses greedy best-first approach
        
        ### 🌳 **Decision Tree Classifier**
        - Machine learning classifier on Iris dataset
        - Binary classification (Setosa vs. Non-Setosa)
        - Includes visualization and performance metrics
        
        ---
        **Select an algorithm from the sidebar to get started!**
        """)
        
        st.info("💡 **Tip**: You can use default graphs or create your own custom graphs for the search algorithms.")
    
    # Uniform Cost Search
    elif algorithm == "🔍 Uniform Cost Search":
        st.header("🔍 Uniform Cost Search Algorithm")
        st.markdown("Finds the shortest path from start to goal using uniform cost search.")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Graph Configuration")
            use_default = st.radio(
                "Graph option:",
                ["Use Default Graph", "Custom Graph"],
                key="ucs_graph_option"
            )
            
            if use_default == "Use Default Graph":
                graph = get_default_graph()
                st.markdown("**Default Graph:**")
                st.markdown(display_graph(graph))
            else:
                st.markdown("**Enter Custom Graph:**")
                st.markdown("Format: `Node1:Node2:cost,Node3:cost; Node2:Node1:cost,Node4:cost; ...`")
                st.markdown("Example: `A:B:1,C:4; B:A:1,C:2,D:5; C:A:4,B:2,D:1; D:B:5,C:1`")
                graph_input = st.text_area("Graph Input:", height=100, key="ucs_custom_graph")
                
                if graph_input:
                    graph = parse_custom_graph(graph_input)
                    if graph:
                        st.markdown("**Your Graph:**")
                        st.markdown(display_graph(graph))
                    else:
                        st.error("Invalid graph format! Using default graph.")
                        graph = get_default_graph()
                else:
                    graph = get_default_graph()
        
        with col2:
            st.subheader("Search Parameters")
            if graph:
                nodes = list(graph.keys())
                start = st.selectbox("Start Node:", nodes, key="ucs_start")
                goal = st.selectbox("Goal Node:", nodes, key="ucs_goal")
                
                if st.button("🔍 Run Uniform Cost Search", type="primary", key="ucs_run"):
                    with st.spinner("Searching for optimal path..."):
                        result, visited = uniform_cost_search(graph, start, goal)
                    
                    if result:
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)
                        st.success("✅ Path Found!")
                        st.markdown(f"**Path:** {' → '.join(result)}")
                        st.markdown(f"**Total Cost:** {calculate_path_cost(graph, result)}")
                        st.markdown(f"**Visited Nodes:** {', '.join(sorted(visited))}")
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.error("❌ Goal state not reachable.")
                        st.info(f"Visited nodes: {', '.join(sorted(visited))}")
    
    # Greedy Search
    elif algorithm == "🎯 Greedy Search":
        st.header("🎯 Greedy Search Algorithm")
        st.markdown("Finds a path using greedy best-first search with heuristic function.")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Graph Configuration")
            use_default = st.radio(
                "Graph option:",
                ["Use Default Graph", "Custom Graph"],
                key="greedy_graph_option"
            )
            
            if use_default == "Use Default Graph":
                graph = get_greedy_graph()
                st.markdown("**Default Graph:**")
                st.markdown(display_graph(graph))
            else:
                st.markdown("**Enter Custom Graph:**")
                st.markdown("Format: `Node1:Node2:cost,Node3:cost; Node2:Node1:cost,Node4:cost; ...`")
                graph_input = st.text_area("Graph Input:", height=100, key="greedy_custom_graph")
                
                if graph_input:
                    graph = parse_custom_graph(graph_input)
                    if graph:
                        st.markdown("**Your Graph:**")
                        st.markdown(display_graph(graph))
                    else:
                        st.error("Invalid graph format! Using default graph.")
                        graph = get_greedy_graph()
                else:
                    graph = get_greedy_graph()
        
        with col2:
            st.subheader("Search Parameters")
            if graph:
                nodes = list(graph.keys())
                start = st.selectbox("Start Node:", nodes, key="greedy_start")
                goal = st.selectbox("Goal Node:", nodes, key="greedy_goal")
                
                st.info("ℹ️ Using alphabetical distance as heuristic function.")
                
                if st.button("🎯 Run Greedy Search", type="primary", key="greedy_run"):
                    heuristic = get_default_heuristic()
                    with st.spinner("Searching for path..."):
                        result, visited = greedy_search(graph, start, goal, heuristic)
                    
                    if result:
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)
                        st.success("✅ Path Found!")
                        st.markdown(f"**Path:** {' → '.join(result)}")
                        st.markdown(f"**Visited Nodes:** {', '.join(sorted(visited))}")
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.error("❌ Goal state not reachable.")
                        st.info(f"Visited nodes: {', '.join(sorted(visited))}")
    
    # Decision Tree Classifier
    elif algorithm == "🌳 Decision Tree Classifier":
        st.header("🌳 Decision Tree Classifier")
        st.markdown("Trains a decision tree classifier on the Iris dataset for binary classification.")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### About the Classifier
            - **Dataset**: Iris (150 samples, 4 features)
            - **Task**: Binary classification (Setosa vs. Non-Setosa)
            - **Model**: Decision Tree Classifier
            - **Train/Test Split**: 80/20
            """)
        
        with col2:
            show_tree = st.checkbox("Show Decision Tree Visualization", value=False)
        
        if st.button("🌳 Train Decision Tree", type="primary", key="dt_run"):
            with st.spinner("Training model..."):
                run_decision_tree_classifier(show_tree)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        Made with ❤️ using Streamlit | AI Project
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
