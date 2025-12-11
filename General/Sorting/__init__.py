

"""
Here is a detailed comparison of their asymptotic complexities and characteristics:

Bubble sort:
    It has a worst-case and average time complexity of O(n2)O(n2).
    It repeatedly swaps adjacent elements if they are in the wrong order.
    Bubble sort is simple but inefficient for large inputs and performs poorly even on partially sorted data.
    Its best case is O(n)O(n) when optimized, but this is still less efficient than heap sort for larger data.


Selection sort:
    It also consistently runs in O(n2)O(n2) time in worst and average cases
    by repeatedly selecting the minimum element from the unsorted part and
    placing it at the front. It performs fewer swaps than bubble sort but
    still has the quadratic time complexity.


Insertion sort:
    It has worst and average cases of O(n2)O(n2), but a best case of O(n)O(n)
    when the array is already sorted. It builds the sorted array incrementally
    by inserting elements into their correct position.
    It is often faster than bubble and selection sort in practice
    due to fewer comparisons and adaptiveness to partially sorted data.

Heap sort:
    It builds a binary heap and extracts the maximum element repeatedly,
    maintaining a consistent O(nlog⁡n)O(nlogn) time complexity regardless of input distribution.
    It is memory efficient and does not degrade in worst cases like bubble or insertion sort.
"""