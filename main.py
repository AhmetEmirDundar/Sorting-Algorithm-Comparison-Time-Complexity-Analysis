from experiments import run_experiments
from visualize import visualize_results

if __name__ == "__main__":
    run_experiments("results/sorting_results.csv")
    visualize_results("results/sorting_results.csv")
