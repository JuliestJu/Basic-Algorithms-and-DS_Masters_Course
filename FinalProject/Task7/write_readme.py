import os
import json

# Determine the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the simulation_data.json file
simulation_data_path = os.path.join(script_dir, 'simulation_data.json')

# Debug print for file paths
print(f"Script directory: {script_dir}")
print(f"Simulation data path: {simulation_data_path}")

# Load the data from the simulation
with open(simulation_data_path, 'r') as f:
    data = json.load(f)

probabilities = data['probabilities']
theoretical_probabilities = data['theoretical_probabilities']
readme_path = data['readme_path']
plot_path = data['plot_path']

# Prepare the content for the readme
readme_content = f"""# Моделювання Монте-Карло для сум двох кубиків

Цей проект моделює кидання двох кубиків велику кількість разів і обчислює ймовірності кожної можливої суми за допомогою методу Монте-Карло. Результати потім порівнюються з теоретичними ймовірностями.

## Змодельовані та теоретичні ймовірності

| Сума | Змодельована ймовірність | Теоретична ймовірність |
|------|---------------------------|------------------------|
"""

for sum_ in sorted(probabilities.keys()):
    readme_content += f"| {sum_:>4} | {probabilities[sum_]:>20.4%} | {theoretical_probabilities[sum_]:>25.4%} |\n"

readme_content += f"""
## Висновок

Змодельовані ймовірності близько відповідають теоретичним ймовірностям, що демонструє точність методу Монте-Карло для цієї задачі. Незначні відмінності обумовлені випадковістю та кількістю виконаних симуляцій.

## Графік ймовірностей

Нижче наведено графік, що порівнює змодельовані та теоретичні ймовірності сум чисел на двох кубиках:

![Графік ймовірностей]({plot_path})
"""

# Write the content to readme.md in the script's directory
with open(readme_path, 'w') as f:
    f.write(readme_content)
