import pandas as pd
import numpy as np
import random
import time

# Load the pre-sorted data
df = pd.read_csv("sorted_quick.csv")

# Extract numeric customer IDs
sorted_ids_numeric = np.array([int(i[1:]) for i in df['customer_id'].astype(str)])

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
def benchmark_search_epochs(search_func, arr, targets, epochs=10):
    times = []
    for _ in range(epochs):
        start = time.perf_counter()
        for target in targets:
            search_func(arr, target)
        end = time.perf_counter()
        times.append((end - start) * 1000)  # ms
    return times

# Generate target values
target_count = len(sorted_ids_numeric)
random_targets = [random.choice(sorted_ids_numeric) for _ in range(target_count)]
uniform_targets = list(np.linspace(sorted_ids_numeric[0], sorted_ids_numeric[-1], target_count, dtype=int))

# Run benchmarks
results = {
    "binary_random": benchmark_search_epochs(binary_search, sorted_ids_numeric, random_targets),
    "binary_uniform": benchmark_search_epochs(binary_search, sorted_ids_numeric, uniform_targets),
    "interpolation_random": benchmark_search_epochs(interpolation_search, sorted_ids_numeric, random_targets),
    "interpolation_uniform": benchmark_search_epochs(interpolation_search, sorted_ids_numeric, uniform_targets)
}

# Print best, average, and worst case times
for key, times in results.items():
    best = min(times)
    avg = sum(times) / len(times)
    worst = max(times)
    print(f"{key}:")
    print(f"  Best  : {best:.3f} ms")
    print(f"  Avg   : {avg:.3f} ms")
    print(f"  Worst : {worst:.3f} ms")