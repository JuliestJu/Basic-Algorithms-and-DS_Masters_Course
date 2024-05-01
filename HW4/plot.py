
import matplotlib.pyplot as plt

# Data from the user
data = {
    "RANDOM": {
        10: {"Insertion Sort": 0.001606292000360554, "Merge Sort": 0.004841917001613183, "Timsort": 0.000310792001982918},
        100: {"Insertion Sort": 0.08081854099873453, "Merge Sort": 0.057109416997263907, "Timsort": 0.0027079170031356625},
        1000: {"Insertion Sort": 9.89434595900093, "Merge Sort": 0.8321509579982376, "Timsort": 0.044770832999347476}
    },
    "SORTED": {
        10: {"Insertion Sort": 0.0004109999972570222, "Merge Sort": 0.0034322089995839633, "Timsort": 0.00013462499919114634},
        100: {"Insertion Sort": 0.0037033749977126718, "Merge Sort": 0.05102000000260887, "Timsort": 0.0005935000008321367},
        1000: {"Insertion Sort": 0.05311420799989719, "Merge Sort": 0.661821041998337, "Timsort": 0.004102582999621518}
    },
    "REVERSE_SORTED": {
        10: {"Insertion Sort": 0.0017618339988985099, "Merge Sort": 0.0035934160005126614, "Timsort": 0.00022158300271257758},
        100: {"Insertion Sort": 0.15144066699940595, "Merge Sort": 0.05168879199845833, "Timsort": 0.003382541999599198},
        1000: {"Insertion Sort": 19.304640458001813, "Merge Sort": 0.6896797080007673, "Timsort": 0.0400466659993981}
    },
    "NEARLY_SORTED": {
        10: {"Insertion Sort": 0.0006021669978508726, "Merge Sort": 0.003524957999616163, "Timsort": 0.0001965000010386575},
        100: {"Insertion Sort": 0.026254832999256905, "Merge Sort": 0.05499095800041687, "Timsort": 0.0021707080013584346},
        1000: {"Insertion Sort": 2.4237770840009034, "Merge Sort": 0.7622234579976066, "Timsort": 0.02916745800030185}
    }
}

# Plotting
fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
fig.suptitle('Sorting Algorithm Performance by Dataset Type', fontsize=16)

# Helper function to plot each dataset type
def plot_data(ax, data, title):
    sizes = sorted(data.keys())
    for algorithm in ["Insertion Sort", "Merge Sort", "Timsort"]:
        times = [data[size][algorithm] for size in sizes]
        ax.plot(sizes, times, marker='o', label=algorithm)
    ax.set_title(title)
    ax.set_xlabel('Dataset Size')
    ax.set_ylabel('Time (seconds)')
    ax.legend()

# Plots for each dataset type
plot_data(axes[0, 0], data["RANDOM"], "Random Data")
plot_data(axes[0, 1], data["SORTED"], "Sorted Data")
plot_data(axes[1, 0], data["REVERSE_SORTED"], "Reverse Sorted Data")
plot_data(axes[1, 1], data["NEARLY_SORTED"], "Nearly Sorted Data")

# Layout adjustments
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust spacing to prevent clipping of title and labels
plt.show()