import timeit
import pandas as pd
import matplotlib.pyplot as plt

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

text1 = load_text('/Users/julia/Developer/PythonProjects/Algs_and_DS_Masters/HW5/HW5.3/article1.txt')
text2 = load_text('/Users/julia/Developer/PythonProjects/Algs_and_DS_Masters/HW5/HW5.3/article2.txt')

# Define substrings for testing
existing_substring = 'алгоритми сортування'
non_existing_substring = 'віддалена галактика'

def run_test(text, pattern, algorithm):
    if algorithm == 'boyer_moore_search':
        module = 'boyer_moore'
    elif algorithm == 'kmp_search':
        module = 'knuth_morris_pratt'
    elif algorithm == 'rabin_karp_search':
        module = 'rabin_karp'
    
    setup_code = f"from {module} import {algorithm}"
    stmt_code = f'''{algorithm}("""{text}""", """{pattern}""")'''
    times = timeit.repeat(setup=setup_code, stmt=stmt_code, repeat=5, number=10)
    return min(times)

algorithms = {
    'Boyer-Moore': 'boyer_moore_search',
    'Knuth-Morris-Pratt': 'kmp_search',
    'Rabin-Karp': 'rabin_karp_search'
}

# Function to plot results for a specific article
def plot_results(article_text, article_name, ax):
    results = {}
    for name, func in algorithms.items():
        results[name] = {
            'Existing substring': run_test(article_text, existing_substring, func),
            'Non-existing substring': run_test(article_text, non_existing_substring, func),
        }

    # Convert results to a DataFrame for easier plotting
    df = pd.DataFrame(results).T
    df.columns = ['Existing Substring', 'Non-existing Substring']

    # Plotting
    df.plot(kind='bar', ax=ax, title=f"Performance of Substring Search Algorithms ({article_name})")
    ax.set_xlabel("Algorithm")
    ax.set_ylabel("Time (seconds)")
    ax.tick_params(rotation=45)

    print(f"\n{article_name} results:")
    print(df)

# Create a figure and axis object for subplots
fig, axs = plt.subplots(1, 2, figsize=(7, 6))

# Plot results for each article
plot_results(text1, 'Article 1', axs[0])
plot_results(text2, 'Article 2', axs[1])

# Adjust layout and display plot
plt.tight_layout()
plt.show()