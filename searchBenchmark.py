import pandas as pd
import numpy as np
import random
import time

# Load the data
df = pd.read_csv("customer_shopping_data_1000.csv")

ids_numeric = np.array([int(i[1:]) for i in df['customer_id'].astype(str).unique()])
sorted_ids_numeric = np.sort(ids_numeric, kind='quicksort')

# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Interpolation Search
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if arr[high] == arr[low]:
            break
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if pos >= len(arr):
            break
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Benchmark function
def benchmark_search(search_func, arr, targets):
    start = time.perf_counter()
    for target in targets:
        search_func(arr, target)
    end = time.perf_counter()
    return (end - start) * 1000  # convert seconds to ms


# Generate target values
target_count = len(sorted_ids_numeric)
random_targets = [random.choice(sorted_ids_numeric) for _ in range(target_count)]
uniform_targets = list(np.linspace(sorted_ids_numeric[0], sorted_ids_numeric[-1], target_count, dtype=int))

# Run benchmarks
results = {
    "binary_random": benchmark_search(binary_search, sorted_ids_numeric, random_targets),
    "binary_uniform": benchmark_search(binary_search, sorted_ids_numeric, uniform_targets),
    "interpolation_random": benchmark_search(interpolation_search, sorted_ids_numeric, random_targets),
    "interpolation_uniform": benchmark_search(interpolation_search, sorted_ids_numeric, uniform_targets)
}

for key, value in results.items():
    print(f"{key}: {value:.3f} ms")