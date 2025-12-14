import csv
import random
from algorithms import merge_sort, heap_sort, insertion_sort, selection_sort

def generate_data(n, dist="random"):
    if dist == "sorted":
        return list(range(n))
    elif dist == "reversed":
        return list(range(n, 0, -1))
    elif dist == "nearly":
        arr = list(range(n))
        swaps = int(0.05 * n)
        for _ in range(swaps):
            i, j = random.sample(range(n), 2)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    else:
        return [random.randint(0, n * 10) for _ in range(n)]


def run_experiments(output_csv="results/sorting_results.csv"):
    algorithms = {
        "merge": merge_sort,
        "heap": heap_sort,
        "insertion": insertion_sort,
        "selection": selection_sort,
    }

    distributions = ["random", "sorted", "reversed", "nearly"]
    sizes = [100, 500, 1000, 2000]

    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algo", "n", "distribution", "pivot", "trial", "time_ms", "comparisons", "swaps", "extra_bytes"])

        for n in sizes:
            for dist in distributions:
                base_data = generate_data(n, dist)
                for algo_name, algo_func in algorithms.items():
                    for trial in range(3):
                        result, metrics = algo_func(base_data)
                        writer.writerow([algo_name, n, dist, "", trial + 1,
                                         round(metrics["time_ms"], 4),
                                         metrics["comparisons"], metrics["swaps"], metrics["extra_bytes"]])
    print(f"Experiments finished. Results saved to {output_csv}")
