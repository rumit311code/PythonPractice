def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1  # Target not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
result = binary_search(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

"""
Time complexity: O(log n) in the worst case, where n is the number of elements in the sorted array. 
This arises because each comparison halves the search space.

Space complexity:
    Iterative implementation: O(1) auxiliary space (constant extra space for indices and a few temporaries).
    Recursive implementation: O(log n) auxiliary space in the worst case due to the call stack depth 
        (each recursive call adds a stack frame).

Key nuances
    Best case: If the target is exactly in the middle on the first check (for some implementations), 
    time can be O(1) in that ideal scenario, but this is not guaranteed for all inputs or implementations.
    
    Average case: Still O(log n) time, with constant space for the iterative version and O(log n) space 
    for the recursive version due to stack depth.
    
    Space considerations: If memory usage is critical (e.g., embedded contexts), prefer the iterative approach 
    for binary search to maintain O(1) space. If recursion is convenient and the input size is modest, 
    the recursive version can be simpler to read, accepting the extra stack space.

Practical takeaway
    For large datasets, expect about log2(n) comparisons in the worst case, and aim for an iterative implementation 
    if you need strict constant extra space. The exact number of steps grows logarithmically with n, not linearly, 
    making binary search highly efficient for sorted arrays.

"""