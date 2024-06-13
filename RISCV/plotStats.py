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
    colors = ['r', 'b', 'g', 'c', 'm', 'y', 'k']  # Lista de colores para asignar a cada archivo
    markers = ['o', 's', 'D', '^', 'v', '<', '>']  # Lista de marcadores para los puntos
    plt.figure(figsize=(12, 8))

    for i, filename in enumerate(stats_files):
        stats = read_relevant_stats(filename)
        x = list(range(len(stats)))
        y = list(stats.values())
        plt.plot(x, y, label=f'File {i+1}', color=colors[i % len(colors)], marker=markers[i % len(markers)], linestyle='-')

    plt.xlabel('Statistic Index')
    plt.ylabel('Value (1x10^6)')
    plt.legend()
    plt.title('Relevant Stats Comparison')
    plt.xticks(x, list(stats.keys()), rotation=90)  # Rotar etiquetas del eje x para mejor legibilidad
    plt.tight_layout()
    plt.show()

def main():
    input_directory = 'relevant_stats'  # Asegúrate de que este directorio contenga tus archivos stats_relevant.txt
    stats_files = [os.path.join(input_directory, filename) for filename in os.listdir(input_directory) if filename.endswith(".txt")]

    if not stats_files:
        print("No relevant stats files found.")
        return

    plot_stats(stats_files)

if __name__ == "__main__":
    main()
