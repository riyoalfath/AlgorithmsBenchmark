import pandas as pd
import numpy as np
import random
import time

# Load data
df = pd.read_csv("customer_shopping_data.csv")

# Convert 'customer_id' to numeric IDs
customer_ids = np.array([int(cid[1:]) for cid in df['customer_id'].astype(str)])

# Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = quick_sort([x for x in arr if x < pivot])
    middle = [x for x in arr if x == pivot]
    right = quick_sort([x for x in arr if x > pivot])
    return left + middle + right

# Benchmark function
def benchmark_sort(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return (end - start) * 1000  # milliseconds

# Run benchmarks on all customer_ids
results = {
    "bubble_sort": benchmark_sort(bubble_sort, customer_ids),
    "quick_sort": benchmark_sort(quick_sort, customer_ids),
}

# Print results
for key, time_ms in results.items():
    print(f"{key}: {time_ms:.3f} ms")