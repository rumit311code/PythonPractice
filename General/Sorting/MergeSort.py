"""
numbers = [38, 27, 43, 10]

Divide:
    [38, 27, 43, 10]  is divided into  [38, 27] and  [43, 10]
    [38, 27]  is divided into  [38]  and  [27]
    [43, 10]  is divided into  [43]  and  [10]
Conquer:
    [38]  is already sorted.
    [27]  is already sorted.
    [43]  is already sorted.
    [10]  is already sorted.
Merge:
    Merge  [38]  and  [27]  to get  [27, 38]
    Merge  [43]  and  [10]  to get  [10,43]
    Merge  [27, 38]  and  [10,43]  to get the final sorted list  [10, 27, 38, 43]

Sorted list = [10, 27, 38, 43]
"""

def merge_sort(arr):
    print(f"arr |{arr}|")
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    print(f"left1 |{left_half}| === right1|{right_half}|")
    return merge(left_half, right_half)

def merge(left, right):
    print(f"left2 |{left}| === right2|{right}|")
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    print(f"sorted_list 1|{sorted_list}|")
    print(f"left[i:] |{left[i:]}| === right[j:]|{right[j:]}|")
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    print(f"sorted_list 2|{sorted_list}|")
    return sorted_list

# Example use
numbers = [38, 27, 43, 10]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)


"""
Time Complexity:
    Best Case: O(n log n), When the array is already sorted or nearly sorted.
    Average Case: O(n log n), When the array is randomly ordered.
    Worst Case: O(n log n), When the array is sorted in reverse order. 

Auxiliary Space: O(n), Additional space is required for the temporary array used during merging.

Applications of Merge Sort:
    Sorting large datasets
    External sorting (when the dataset is too large to fit in memory)
    Used to solve problems like Inversion counting, Count Smaller on Right & Surpasser Count
    Merge Sort and its variations are used in library methods of programming languages. 
        Its variation TimSort is used in Python, Java Android and Swift. The main reason why it is preferred 
        to sort non-primitive types is stability which is not there in QuickSort. 
        Arrays.sort in Java uses QuickSort while Collections.sort uses MergeSort.
    It is a preferred algorithm for sorting Linked lists.
    It can be easily parallelized as we can independently sort subarrays and then merge.
    The merge function of merge sort to efficiently solve the problems like union and intersection of two sorted arrays.

Advantages
    Stability : Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.
    Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(N logN) , 
        which means it performs well even on large datasets.
    Simple to implement: The divide-and-conquer approach is straightforward.
    Naturally Parallel : We independently merge subarrays that makes it suitable for parallel processing.

Disadvantages
    Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process.
    Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to 
        store the sorted data. This can be a disadvantage in applications where memory usage is a concern.
    Merge Sort is Slower than QuickSort in general as QuickSort is more cache friendly because it works in-place.
"""