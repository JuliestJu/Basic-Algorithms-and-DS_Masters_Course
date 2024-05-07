import networkx as nx
import matplotlib.pyplot as plt
from graph_creation import create_kyiv_subway_graph


G = create_kyiv_subway_graph()
# Create a color map based on the 'line' attribute
color_map = []
for node in G:
    if G.nodes[node]['line'] == 'Red':
        color_map.append('red')
    elif G.nodes[node]['line'] == 'Blue':
        color_map.append('blue')
    elif G.nodes[node]['line'] == 'Green':
        color_map.append('green')

# Analyzing the graph
print("Number of stations:", G.number_of_nodes())
print("Number of connections:", G.number_of_edges())
print("Degree of each station:", dict(G.degree()))

# Determine positions for the nodes (this might need further adjustment for better visualization)
pos = nx.spring_layout(G, iterations = 3000)

# Drawing the nodes
nx.draw_networkx_nodes(G, pos, node_color = color_map, node_size = 50)

# Adjust label positions to be slightly above the nodes
label_pos = { key: [value[0], value[1] + 0.05] for key, value in pos.items() }

# Drawing the labels using adjusted positions
nx.draw_networkx_labels(G, label_pos, font_size = 9, font_color = 'black')

# Define interchange connections for special coloring
interchange_edges = [("Золоті ворота", "Театральна"),
                     ("Майдан Незалежності", "Хрещатик"),
                     ("Палац спорту", "Площа Українських Героїв")]

# Create edge colors
edge_colors = []
for u, v in G.edges():
    if (u, v) in interchange_edges or (v, u) in interchange_edges:
        edge_colors.append('#741b47')
    elif G.nodes[u]['line'] == G.nodes[v]['line']:
        if G.nodes[u]['line'] == 'Red':
            edge_colors.append('#df9c97')
        elif G.nodes[u]['line'] == 'Blue':
            edge_colors.append('#45c7e4')
        elif G.nodes[u]['line'] == 'Green':
            edge_colors.append('#a7e78a')
    else:
        edge_colors.append('lightgray')  # Default color

nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
plt.show()
