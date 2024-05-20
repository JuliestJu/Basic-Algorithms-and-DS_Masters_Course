
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        self.vertices[name] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        # Since it's a directed graph
        self.vertices[from_vertex].append((to_vertex, weight))

    def dijkstra(self, start_vertex):
        # Distances dictionary
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0

        # Priority queue (min-heap)
        priority_queue = []
        heapq.heappush(priority_queue, (0, start_vertex))

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            # Consider each adjacent node
            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                # Only consider this new path if it's better
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Usage
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A', 'B', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'C', 4)
graph.add_edge('C', 'D', 1)
graph.add_edge('B', 'D', 5)

print("Shortest Paths from A:", graph.dijkstra('A'))

