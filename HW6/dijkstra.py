
import heapq
from graph_creation import create_kyiv_subway_graph

def dijkstra(graph, start):
    # Initialize distances dictionary with infinite distance for all nodes
    distances = {node: float('inf') for node in graph}
    # Set distance to the start node to 0
    distances[start] = 0
    # Priority queue to keep track of nodes to visit next
    queue = [(0, start)]  # (distance, node)
    
    while queue:
        # Pop node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(queue)
        
        # If current distance is greater than distance in distances, skip
        if current_distance > distances[current_node]:
            continue
        
        # Iterate through neighbors of the current node
        for neighbor in graph[current_node]:
            # Calculate the new distance
            distance = current_distance + 1  # Assuming equal weight for all edges
            
            # If new distance is shorter than current distance to neighbor, update distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add neighbor to the priority queue with updated distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Create the subway graph
subway_graph = create_kyiv_subway_graph()

# Add weights to the edges (assuming equal weight for all edges)
for edge in subway_graph.edges:
    subway_graph.edges[edge]['weight'] = 1

# Call Dijkstra's algorithm for each node as the starting point
shortest_paths = {}
for node in subway_graph.nodes:
    shortest_paths[node] = dijkstra(subway_graph, node)

# Print shortest paths
for start_node in shortest_paths:
    print(f"Shortest paths from {start_node}:")
    for end_node, distance in shortest_paths[start_node].items():
        print(f"To {end_node}: {distance} stations")
    print()