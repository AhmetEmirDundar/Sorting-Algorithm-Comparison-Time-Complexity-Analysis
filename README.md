# Algorithms Project

## Overview

This project provides a comprehensive performance analysis and comparison of four classic sorting algorithms: **Merge Sort**, **Heap Sort**, **Insertion Sort**, and **Selection Sort**. The project systematically tests these algorithms across different data distributions and input sizes, collecting detailed metrics including execution time, number of comparisons, number of swaps, and memory usage. The results are visualized through interactive charts to help understand the performance characteristics of each algorithm.

### Key Features

- **Four Sorting Algorithms**: Implementation of merge sort, heap sort, insertion sort, and selection sort
- **Multiple Data Distributions**: Tests on random, sorted, reversed, and nearly sorted data
- **Comprehensive Metrics**: Tracks runtime, comparisons, swaps, and memory usage
- **Visualization**: Generates log-scale runtime comparison charts
- **Reproducible Experiments**: Multiple trials per configuration for statistical reliability

## Algorithms Implemented

### 1. Merge Sort
- **Type**: Divide and conquer
- **Time Complexity**: O(n log n) in all cases
- **Space Complexity**: O(n) - requires additional memory for merging
- **Characteristics**: Stable, efficient for large datasets, consistent performance

### 2. Heap Sort
- **Type**: Comparison-based, uses binary heap
- **Time Complexity**: O(n log n) in all cases
- **Space Complexity**: O(1) - in-place sorting
- **Characteristics**: Not stable, guaranteed O(n log n) performance, no worst-case degradation

### 3. Insertion Sort
- **Type**: Simple iterative
- **Time Complexity**: O(n²) worst/average, O(n) best (nearly sorted)
- **Space Complexity**: O(1) - in-place sorting
- **Characteristics**: Stable, adaptive, efficient for small datasets or nearly sorted data

### 4. Selection Sort
- **Type**: Simple iterative
- **Time Complexity**: O(n²) in all cases
- **Space Complexity**: O(1) - in-place sorting
- **Characteristics**: Not stable, simple implementation, always performs the same regardless of input

## Project Structure

```
Algorithms Project/
├── algorithms.py          # Sorting algorithm implementations with metric tracking
├── experiments.py         # Experiment runner - generates data and runs tests
├── visualize.py           # Visualization module for plotting results
├── main.py                # Main entry point - runs experiments and visualization
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── results/               # Generated output files
    ├── sorting_results.csv        # Detailed experiment results
    ├── runtime_comparison.png      # Runtime visualization chart
    └── df.ipynb                   # Jupyter notebook for custom analysis
```

## File Descriptions

### `algorithms.py`
Contains the implementations of all four sorting algorithms. Each algorithm is wrapped with a `@measure_time` decorator that automatically tracks:
- **Execution time** (in milliseconds)
- **Number of comparisons** between elements
- **Number of swaps** performed
- **Extra memory usage** (bytes) for algorithms that require additional space

### `experiments.py`
The experiment framework that:
- Generates test data in four distributions:
  - **Random**: Completely random integers
  - **Sorted**: Already sorted ascending order
  - **Reversed**: Sorted in descending order
  - **Nearly sorted**: 95% sorted with 5% random swaps
- Tests each algorithm on multiple input sizes: 100, 500, 1000, 2000 elements
- Runs 3 trials per configuration for statistical reliability
- Exports results to CSV format with all metrics

### `visualize.py`
Creates visualizations of the experimental results:
- Generates log-scale line plots comparing runtime across algorithms
- Uses seaborn and matplotlib for professional-quality charts
- Saves plots as PNG files in the results directory

### `main.py`
Simple entry point that orchestrates the entire workflow:
1. Runs all experiments
2. Generates visualizations
3. Saves all outputs to the results directory

## Setup Instructions

### Prerequisites
- **Python 3.10 or higher** (tested with Python 3.10+)
- **pip** package manager

### Installation

1. **Clone or download this project** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd "Algorithms Project"
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   This will install:
   - `pandas` (>=2.2.0) - Data manipulation and CSV handling
   - `matplotlib` (>=3.8.0) - Plotting and visualization
   - `seaborn` (>=0.13.0) - Statistical data visualization

## Usage

### Running Complete Analysis

To run all experiments and generate visualizations in one command:

```bash
python main.py
```

This will:
1. Generate test data for all distributions and sizes
2. Run each algorithm on all test cases (3 trials each)
3. Save detailed results to `results/sorting_results.csv`
4. Generate and save the runtime comparison chart to `results/runtime_comparison.png`
5. Display the chart in a window

**Expected runtime**: A few seconds to a minute depending on your system

### Running Only Visualization

If you already have results in CSV format and only want to regenerate the plots:

```bash
python -c "from visualize import visualize_results; visualize_results('results/sorting_results.csv')"
```

Or from Python:
```python
from visualize import visualize_results
visualize_results('results/sorting_results.csv')
```

### Running Individual Components

You can also run components separately:

**Run experiments only:**
```python
from experiments import run_experiments
run_experiments('results/sorting_results.csv')
```

**Test a single algorithm:**
```python
from algorithms import merge_sort
result, metrics = merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Sorted: {result}")
print(f"Metrics: {metrics}")
```

## Output Files

### `results/sorting_results.csv`

A CSV file containing detailed results for every experiment run. Columns include:
- `algo`: Algorithm name (merge, heap, insertion, selection)
- `n`: Input size (number of elements)
- `distribution`: Data distribution type (random, sorted, reversed, nearly)
- `pivot`: Reserved for future use (currently empty)
- `trial`: Trial number (1-3)
- `time_ms`: Execution time in milliseconds
- `comparisons`: Number of element comparisons performed
- `swaps`: Number of element swaps performed
- `extra_bytes`: Additional memory used (0 for in-place algorithms)

### `results/runtime_comparison.png`

A log-scale line chart showing:
- X-axis: Input size (n) on logarithmic scale
- Y-axis: Execution time (ms) on logarithmic scale
- Multiple lines: One for each algorithm
- Markers: Data points for each tested input size

This visualization makes it easy to see:
- Which algorithms scale better with larger inputs
- Performance differences between algorithms
- How algorithms behave across different input sizes

## Understanding the Results

### Expected Performance Patterns

1. **Small datasets (n < 500)**:
   - Insertion sort may perform competitively, especially on nearly sorted data
   - Selection sort shows consistent O(n²) behavior

2. **Large datasets (n > 1000)**:
   - Merge sort and heap sort show their O(n log n) advantage
   - Insertion and selection sort show quadratic growth

3. **Data distribution effects**:
   - **Sorted data**: Insertion sort excels (O(n))
   - **Reversed data**: All algorithms show worst-case behavior
   - **Nearly sorted**: Insertion sort benefits from adaptivity
   - **Random data**: Best case for comparing general performance

### Interpreting Metrics

- **Time (ms)**: Actual wall-clock execution time - most important for practical applications
- **Comparisons**: Number of element comparisons - indicates algorithmic efficiency
- **Swaps**: Number of element swaps - relevant for memory-intensive operations
- **Extra bytes**: Memory overhead - merge sort uses O(n) extra space, others are in-place

## Custom Analysis

For deeper analysis, you can:

1. **Open the CSV in Excel or any spreadsheet application** for filtering and sorting

2. **Use the Jupyter notebook** (`results/df.ipynb`) for interactive analysis:
   ```bash
   jupyter notebook results/df.ipynb
   ```

3. **Modify experiment parameters** in `experiments.py`:
   - Change input sizes: Modify the `sizes` list
   - Add more trials: Change the `range(3)` value
   - Add new distributions: Extend the `generate_data()` function

4. **Create custom visualizations** by modifying `visualize.py`:
   - Compare specific metrics (comparisons, swaps)
   - Filter by distribution type
   - Create separate charts for each distribution

## Technical Details

### Metric Collection

All algorithms use a consistent metric collection system:
- Metrics are tracked during algorithm execution
- Time measurement uses `time.perf_counter()` for high precision
- Input arrays are copied before sorting to ensure fair comparisons
- Memory usage is estimated (merge sort: 4 bytes per element for temporary arrays)

### Algorithm Correctness

All implementations:
- Sort arrays in ascending order
- Handle edge cases (empty arrays, single elements)
- Preserve all elements (no data loss)
- Return both sorted array and metrics dictionary

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed (`pip install -r requirements.txt`)

2. **File not found errors**: Ensure the `results/` directory exists (it should be created automatically)

3. **Plot not displaying**: If using a headless environment, the plot will still be saved to file

4. **Slow execution**: Large input sizes or many trials will take longer. Adjust parameters in `experiments.py` if needed

## Future Enhancements

Potential additions to this project:
- Quick Sort implementation
- More data distributions (duplicates, specific patterns)
- Additional metrics (cache misses, branch predictions)
- Interactive web-based visualization
- Statistical analysis (mean, median, standard deviation across trials)
- Comparison with built-in Python `sorted()` function

## License

This project is provided as-is for educational and research purposes.

## Contributing

Feel free to extend this project with:
- Additional sorting algorithms
- New visualization types
- Performance optimizations
- Documentation improvements

---

**Note**: This project is designed for educational purposes to understand algorithm performance characteristics. For production use, consider using optimized libraries like Python's built-in `sorted()` or NumPy's sorting functions.
