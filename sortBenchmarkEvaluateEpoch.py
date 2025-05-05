import pandas as pd
import numpy as np
import random
import time

# Load data
df = pd.read_csv("customer_shopping_data.csv")
customer_ids = np.array([int(cid[1:]) for cid in df['customer_id'].astype(str).unique()])

# Generate random and uniform subsets, you can change to what you want to search
random_data = np.array([random.choice(customer_ids) for _ in range(1000)])
uniform_data = np.linspace(customer_ids.min(), customer_ids.max(), 1000, dtype=int)

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

# Benchmark function (100 epochs)
def benchmark_sort(sort_func, arr, epochs=100):
    total_time = 0
    for _ in range(epochs):
        total_time += benchmark_single_epoch(sort_func, arr)
    return total_time / epochs  # Average time in milliseconds

def benchmark_single_epoch(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return (end - start) * 1000  # milliseconds

# Run benchmarks
results = {
    "bubble_sort_random": benchmark_sort(bubble_sort, random_data),
    "bubble_sort_uniform": benchmark_sort(bubble_sort, uniform_data),
    "quick_sort_random": benchmark_sort(quick_sort, random_data),
    "quick_sort_uniform": benchmark_sort(quick_sort, uniform_data),
}

# Print results
for key, time_ms in results.items():
    print(f"{key}: {time_ms:.3f} ms (average over 100 epochs)")