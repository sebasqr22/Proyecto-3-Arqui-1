import os
import matplotlib.pyplot as plt

def read_relevant_stats(filename):
    stats = {}
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.strip().split(": ")
            stats[key.strip()] = float(value)
    return stats

def plot_stats(stats_files):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Lista de colores para asignar a cada archivo
    for i, filename in enumerate(stats_files):
        stats = read_relevant_stats(filename)
        x = range(len(stats))
        plt.plot(x, list(stats.values()), label=f'File {i+1}', color=colors[i % len(colors)])

    plt.xlabel('Statistic Index')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Relevant Stats Comparison')
    plt.show()

def main():
    input_directory = 'relevant_stats'
    stats_files = [os.path.join(input_directory, filename) for filename in os.listdir(input_directory) if filename.endswith(".txt")]

    if not stats_files:
        print("No relevant stats files found.")
        return

    plot_stats(stats_files)

if __name__ == "__main__":
    main()
