"""
Algorithm Analysis Project: Quick Sort and Heap Sort
Language: Python

Both sorting functions return a sorted copy and leave the input list unchanged.
Run correctness tests:
    python quick_sort_heap_sort.py
Run the performance experiment:
    python quick_sort_heap_sort.py --benchmark
"""

import argparse
import platform
import random
import statistics
import sys
import time


def quick_sort(arr):
    """Return a sorted copy of arr using Quick Sort."""
    items = arr.copy()

    def partition(low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, len(items) - 1)
    return items


def heap_sort(arr):
    """Return a sorted copy of arr using Heap Sort."""
    items = arr.copy()
    n = len(items)

    def heapify(heap_size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < heap_size and items[left] > items[largest]:
            largest = left
        if right < heap_size and items[right] > items[largest]:
            largest = right

        if largest != root:
            items[root], items[largest] = items[largest], items[root]
            heapify(heap_size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for end in range(n - 1, 0, -1):
        items[0], items[end] = items[end], items[0]
        heapify(end, 0)

    return items


def run_tests():
    """Run representative correctness tests for both algorithms."""
    test_cases = [
        [],
        [1],
        [5, 2, 8, 1, 3],
        [4, 4, 4, 4],
        [9, 7, 5, 3, 1],
        [1, 2, 3, 4, 5],
        [-3, 0, 7, -1, 2],
        [3, -2, 3, 0, -2, 8, 1],
    ]

    for values in test_cases:
        expected = sorted(values)
        assert quick_sort(values) == expected
        assert heap_sort(values) == expected

    print(f"All {len(test_cases)} test cases passed for both algorithms.")


def run_benchmark():
    """
    Compare median execution times over seven trials.
    Data creation and correctness checking are outside the timed interval.
    """
    sizes = [100, 300, 600, 900]
    patterns = ["Random", "Ascending", "Descending"]
    rng = random.Random(20261025)

    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print("Time unit: milliseconds; statistic: median of 7 trials")
    print("n, pattern, Quick Sort (ms), Heap Sort (ms)")

    for n in sizes:
        base = [rng.randint(-100000, 100000) for _ in range(n)]
        data_by_pattern = {
            "Random": base,
            "Ascending": sorted(base),
            "Descending": sorted(base, reverse=True),
        }

        for pattern in patterns:
            values = data_by_pattern[pattern]
            expected = sorted(values)
            row = []
            for algorithm in (quick_sort, heap_sort):
                samples = []
                for _ in range(7):
                    start = time.perf_counter()
                    result = algorithm(values)
                    samples.append((time.perf_counter() - start) * 1000)
                    assert result == expected
                row.append(statistics.median(samples))
            print(f"{n}, {pattern}, {row[0]:.3f}, {row[1]:.3f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quick Sort and Heap Sort analysis")
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="run the timing experiment instead of correctness tests",
    )
    args = parser.parse_args()

    if args.benchmark:
        run_benchmark()
    else:
        run_tests()
