def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
"""
Complexities
    Time Complexity:
        Worst case: O(n^2)
        Average case: O(n^2)
        Best case (already sorted): O(n)

    Space Complexity: O(1) (in-place sorting)

Applications
    Teaching and demonstration of sorting concepts due to simplicity
    Works well with small or nearly sorted data sets in simple educational or experimental contexts

Pros
    Simple and easy to implement and understand
    Adaptive (best case O(n) if array is already sorted)
    In-place algorithm with constant space complexity

Cons
    Very inefficient for large data sets compared to advanced algorithms
    Repeatedly compares and swaps adjacent elements leading to high overhead
    Practically replaced by faster algorithms for production use
"""