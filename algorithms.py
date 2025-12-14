import time
from typing import List, Dict, Callable


def measure_time(func: Callable) -> Callable:
    """Decorator to measure time and count metrics."""
    def wrapper(arr):
        start = time.perf_counter()
        result, metrics = func(arr.copy())
        end = time.perf_counter()
        metrics["time_ms"] = (end - start) * 1000
        return result, metrics
    return wrapper


@measure_time
def insertion_sort(arr: List[int]):
    metrics = {"comparisons": 0, "swaps": 0, "extra_bytes": 0}
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            metrics["comparisons"] += 1
            arr[j + 1] = arr[j]
            metrics["swaps"] += 1
            j -= 1
        if j >= 0:
            metrics["comparisons"] += 1
        arr[j + 1] = key
    return arr, metrics


@measure_time
def selection_sort(arr: List[int]):
    metrics = {"comparisons": 0, "swaps": 0, "extra_bytes": 0}
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            metrics["comparisons"] += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            metrics["swaps"] += 1
    return arr, metrics


def merge(left, right, metrics):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        metrics["comparisons"] += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            metrics["swaps"] += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


@measure_time
def merge_sort(arr: List[int]):
    metrics = {"comparisons": 0, "swaps": 0, "extra_bytes": len(arr) * 4}

    def _merge_sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = _merge_sort(a[:mid])
        right = _merge_sort(a[mid:])
        return merge(left, right, metrics)

    sorted_arr = _merge_sort(arr)
    return sorted_arr, metrics


@measure_time
def heap_sort(arr: List[int]):
    metrics = {"comparisons": 0, "swaps": 0, "extra_bytes": 0}

    def heapify(n, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < n:
            metrics["comparisons"] += 1
            if arr[l] > arr[largest]:
                largest = l
        if r < n:
            metrics["comparisons"] += 1
            if arr[r] > arr[largest]:
                largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            metrics["swaps"] += 1
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        metrics["swaps"] += 1
        heapify(i, 0)
    return arr, metrics
