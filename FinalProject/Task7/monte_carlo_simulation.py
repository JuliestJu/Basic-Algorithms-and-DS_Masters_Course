import random
import matplotlib.pyplot as plt
import os
import json
import sys
import subprocess

def simulate_dice_throws(n_throws):
    sums_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(n_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_counts[dice_sum] += 1
    
    probabilities = {sum_: count / n_throws for sum_, count in sums_counts.items()}
    
    return sums_counts, probabilities

def plot_probabilities(probabilities, theoretical_probabilities, image_path):
    sums = sorted(probabilities.keys())
    sim_probs = [probabilities[sum_] for sum_ in sums]
    theo_probs = [theoretical_probabilities[sum_] for sum_ in sums]
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, sim_probs, width=0.4, label='Simulated Probabilities', align='center')
    plt.bar([s + 0.4 for s in sums], theo_probs, width=0.4, label='Theoretical Probabilities', align='center')
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Probabilities of Sums of Two Dice Throws')
    plt.xticks(sums)
    plt.legend()
    plt.savefig(image_path)  # Save the plot as an image
    plt.close()

# Number of throws for the Monte Carlo simulation
n_throws = 100000

# Simulate dice throws
sums_counts, probabilities = simulate_dice_throws(n_throws)

# Theoretical probabilities
theoretical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Print the results in a table format
print(f"{'Sum':>4} {'Simulated Probability':>20} {'Theoretical Probability':>25}")
for sum_ in sorted(probabilities.keys()):
    print(f"{sum_:>4} {probabilities[sum_]:>20.4%} {theoretical_probabilities[sum_]:>25.4%}")

# Determine the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the readme.md file and plot image in the same directory as the script
readme_path = os.path.join(script_dir, 'readme.md')
plot_path = os.path.join(script_dir, 'probabilities_plot.png')
simulation_data_path = os.path.join(script_dir, 'simulation_data.json')

# Debug print for file paths
print(f"Script directory: {script_dir}")
print(f"Plot path: {plot_path}")
print(f"Simulation data path: {simulation_data_path}")

# Save the plot
plot_probabilities(probabilities, theoretical_probabilities, plot_path)

# Save the data for writing the readme
data = {
    'probabilities': probabilities,
    'theoretical_probabilities': theoretical_probabilities,
    'readme_path': readme_path,
    'plot_path': os.path.relpath(plot_path, start=script_dir)  # Save relative path
}

# Save the data to a file for the second script to read
with open(simulation_data_path, 'w') as f:
    json.dump(data, f)

# Automatically run the write_readme.py script using the current Python interpreter
subprocess.run([sys.executable, os.path.join(script_dir, 'write_readme.py')])
