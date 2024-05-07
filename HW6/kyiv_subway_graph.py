import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Adding stations (nodes) for each line
# Red Line
red_line = ["Академмістечко", "Житомирська", "Святошин", "Нивки",
            "Берестейська", "Шулявська", "Політехнічний інститут",
            "Вокзальна", "Університет", "Театральна", "Хрещатик",
            "Арсенальна", "Дніпро", "Гідропарк", "Лівобережна",
            "Дарниця", "Чернігівська", "Лісова"]
# Blue Line
blue_line = ["Героїв Дніпра", "Мінська", "Оболонь", "Почайна",
             "Тараса Шевченка", "Контрактова площа", "Поштова площа",
             "Майдан Незалежності", "Площа Українських Героїв", "Олімпійська", 
             "Палац «Україна»", "Либідська", "Деміївська", "Голосіївська",
             "Васильківська", "Виставковий центр", "Іподром", "Теремки"]
# Green Line
green_line = ["Сирець", "Дорогожичі", "Лук'янівська",
              "Золоті ворота", "Палац спорту", "Кловська",
              "Печерська", "Звіринецька", "Видубичі", "Славутич",
              "Осокорки", "Позняки", "Харківська", "Вирлиця",
              "Бориспільська", "Червоний хутір"]

# Add nodes with line attribute
for station in red_line:
    G.add_node(station, line='Red')
for station in blue_line:
    G.add_node(station, line='Blue')
for station in green_line:
    G.add_node(station, line='Green')

# Connect stations within each line
for line in [red_line, blue_line, green_line]:
    nx.add_path(G, line)

# Adding interchange connections
G.add_edge("Золоті ворота", "Театральна")  # Red to Green
G.add_edge("Майдан Незалежності", "Хрещатик")  # Red to Blue
G.add_edge("Палац спорту", "Площа Українських Героїв")  # Green to Blue

color_map = []
for node in G:
    # Default color if 'line' attribute is missing
    node_color = 'gray'
    if 'line' in G.nodes[node]:
        if G.nodes[node]['line'] == 'Red':
            node_color = 'red'
        elif G.nodes[node]['line'] == 'Blue':
            node_color = 'blue'
        elif G.nodes[node]['line'] == 'Green':
            node_color = 'green'
    color_map.append(node_color)

# Analyzing the graph
print("Number of stations:", G.number_of_nodes())
print("Number of connections:", G.number_of_edges())
print("Degree of each station:", dict(G.degree()))

# Determine positions for the nodes (this might need further adjustment for better visualization)
pos = nx.spring_layout(G, iterations=3000)


# Drawing the graph using the color map
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=50, font_size=8, font_color='black')
plt.show()


