import pandas as pd
import numpy as np
import time

# Load data
df = pd.read_csv("customer_shopping_data_1000.csv")

# Extract numeric parts from customer IDs
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

# Benchmark and return sorted data
def benchmark_sort(sort_func, arr):
    start = time.perf_counter()
    sorted_arr = sort_func(arr)
    end = time.perf_counter()
    time_taken = (end - start) * 1000  # milliseconds
    return time_taken, sorted_arr

# Run benchmarks
results = {}
# time_bubble, sorted_bubble = benchmark_sort(bubble_sort, customer_ids)
time_quick, sorted_quick = benchmark_sort(quick_sort, customer_ids)

# results['bubble_sort'] = time_bubble
results['quick_sort'] = time_quick

# Print benchmark results
for key, time_ms in results.items():
    print(f"{key}: {time_ms:.3f} ms")

# Save to CSV
# pd.DataFrame({'customer_id': [f"C{str(x).zfill(3)}" for x in sorted_bubble]}).to_csv("sorted_bubble.csv", index=False)
pd.DataFrame({'customer_id': [f"C{str(x).zfill(3)}" for x in sorted_quick]}).to_csv("sorted_quick.csv", index=False)