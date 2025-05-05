import pandas as pd
import numpy as np
import time
from tqdm import tqdm

# Load data
df = pd.read_csv("customer_shopping_data.csv")

# Generate random and uniform subsets, you can change to what you want to search
customer_ids = np.array([int(cid[1:]) for cid in df['customer_id'].astype(str)])

# Bubble Sort with tqdm progress bar
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in tqdm(range(n), desc="Bubble Sorting", unit="pass"):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Quick Sort (kept simple, no internal progress tracking)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = quick_sort([x for x in arr if x < pivot])
    middle = [x for x in arr if x == pivot]
    right = quick_sort([x for x in arr if x > pivot])
    return left + middle + right

# Benchmark with real-time elapsed display
def benchmark_sort(sort_func, arr):
    print(f"\nStarting {sort_func.__name__}...")
    start = time.perf_counter()

    result = sort_func(arr)

    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Finished {sort_func.__name__} in {elapsed_ms:.2f} ms")
    return elapsed_ms

# Run benchmarks
results = {
    "bubble_sort": benchmark_sort(bubble_sort, customer_ids),
    "quick_sort": benchmark_sort(quick_sort, customer_ids),
}

# Print summary
print("\n--- Sort Benchmark Results ---")
for key, time_ms in results.items():
    print(f"{key}: {time_ms:.3f} ms")