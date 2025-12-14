import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_results(csv_path="results/sorting_results.csv"):
    df = pd.read_csv(csv_path)

    sns.set(style="whitegrid", font_scale=1.1)

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df[df["algo"] != "quick"], x="n", y="time_ms", hue="algo", marker="o")
    plt.title("Sorting Algorithms Runtime Comparison")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (ms)")
    plt.xscale("log")
    plt.yscale("log")
    plt.tight_layout()
    plt.savefig("results/runtime_comparison.png")
    plt.show()

    print("Plots saved in results/ folder.")
