import networkx as nx

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

# Create a new graph
def create_kyiv_subway_graph():
    G = nx.Graph()
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
    return G


