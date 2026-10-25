# ALGORITHM_ANALYSIS_PROJECT
QUICK SORT AND HEAP SORT
# Quick Sort and Heap Sort — 

## 1. Project Overview

This project implements and analyzes two sorting algorithms in Python: Quick Sort and Heap Sort.

The main objectives are to understand how the algorithms work, analyze their time and auxiliary space complexity, test their correctness, and compare their strengths and limitations.

## 2. Algorithms

### Quick Sort

Quick Sort is a divide-and-conquer sorting algorithm. This implementation selects the last element as the pivot and partitions the list around it. It then recursively sorts the left and right partitions.

- Best-case time complexity: O(n log n)
- Average-case time complexity: O(n log n)
- Worst-case time complexity: O(n²)
- Average auxiliary stack space: O(log n)
- Worst-case auxiliary stack space: O(n)

The choice of pivot can significantly affect performance. Already sorted or reverse-sorted inputs may lead to poor performance in this implementation because the last element is always selected as the pivot.

### Heap Sort

Heap Sort first builds a max heap, in which each parent is greater than or equal to its children. It repeatedly moves the maximum element to the end of the list and restores the heap property.

- Best-case time complexity: O(n log n)
- Average-case time complexity: O(n log n)
- Worst-case time complexity: O(n log n)
- Auxiliary stack space for recursive heapify: O(log n)

Heap Sort provides a predictable worst-case time complexity of O(n log n).

## 3. Project Structure

```text
quick-sort-heap-sort/
├── quick_sort_heap_sort.py
└── README.md
```

## 4. Requirements

- Python 3
- No external packages are required.

## 5. How to Run

Run the Python file from your terminal:

```bash
python quick_sort_heap_sort.py
```

Expected output:

```text
All 8 test cases passed for both algorithms.
```

## 6. Correctness Testing

Both algorithms are tested using eight test cases covering:

- Empty lists
- Single-element lists
- Mixed values
- Duplicate values
- Ascending-order inputs
- Descending-order inputs
- Negative numbers
- Lists containing both positive and negative values

Each algorithm's output is compared with Python's built-in `sorted()` function. The functions return a sorted copy and leave the original input list unchanged.

## 7. Complexity Comparison

| Property | Quick Sort | Heap Sort |
|---|---|---|
| Best-case time | O(n log n) | O(n log n) |
| Average-case time | O(n log n) | O(n log n) |
| Worst-case time | O(n²) | O(n log n) |
| Auxiliary stack space | O(log n) average; O(n) worst case | O(log n) |
| Stable sorting | No | No |

Both functions copy the input list, which requires O(n) additional storage. The auxiliary stack complexities above are considered separately from the input copy.

## 8. Limitations

The current Quick Sort implementation always selects the last element as the pivot. This can create unbalanced partitions and may cause Python's recursion limit to be reached for sufficiently large, already sorted inputs.

A randomized or median-based pivot strategy could reduce this risk. However, randomized pivot selection does not eliminate the theoretical O(n²) worst case.

The Heap Sort implementation uses a recursive `heapify` function, which requires O(log n) stack space.

## 9. Conclusion

Quick Sort often performs well on random inputs but is sensitive to pivot selection. Heap Sort offers a guaranteed O(n log n) worst-case time complexity.

The choice between the algorithms depends on the input data, practical performance requirements, and the importance of a predictable worst-case running time.

## 10. Language and Tools

- Programming language: Python
- Testing reference: Python's built-in `sorted()` function
- Project type: Algorithm analysis and comparison