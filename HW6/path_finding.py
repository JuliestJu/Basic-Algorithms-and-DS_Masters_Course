import networkx as nx
from graph_creation import create_kyiv_subway_graph

# Function to find all paths using DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Function to find all paths using BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Use the graph
subway_graph = create_kyiv_subway_graph()

# Example: Finding paths from '' to ''
start_station = "Теремки"
end_station = "Печерська"
print("DFS paths:")
for path in dfs_paths(subway_graph, start_station, end_station):
    print(path)

print("BFS paths:")
for path in bfs_paths(subway_graph, start_station, end_station):
    print(path)