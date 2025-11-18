"""
QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and
partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

It works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

There are mainly three steps in the algorithm:

1. Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary
    (e.g., first element, last element, random element, or median). Partition the Array: Re arrange the array around the pivot.
    After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot
    will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.

2. Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).

3. Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
"""
Complexities
    Time Complexity:
        Average case: O(nlogn)
        Worst case: O(n^2) (rare, happens when pivot is poorly chosen)

    Space Complexity: O(logn) due to recursion stack

Applications
    Efficient for large datasets
    Used in databases and file systems for sorting large collections of records
    Often used in systems programming and embedded systems due to average efficiency

Pros
    Generally faster in practice than other O(n^2) algorithms
    In-place sorting (some variants)
    Efficient on average

Cons
    Worst-case performance is O(n^2)
    Recursive, which may cause stack overflow for very large arrays if not optimized
"""