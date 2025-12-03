def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1  # Invalid case

    window_sum = sum(arr[:k])  # sum of first window (0,k)
    max_sum = window_sum

    # [1, 8, 30, -5, 20, 7], k=3
    # start with window_sum = max_sum = 1 + 8 + 30 = 39
    for i in range(k, n): # range(3,6)=3,4,5
        print(f"window_sum1: {window_sum}, max_sum1: {max_sum}")
        print(f"i |{i}|===k|{k}|===arr[i]|{arr[i]}|===arr[i-k]|{arr[i-k]}|")

        # loop1:
        #   arr[i]=arr[3]= -5, arr[i-k]=arr[3-3=0]= 1
        #   window_sum = 39+(-5)-(1) = 33. max_sum=39
        # loop2:
        #   arr[i]=arr[4]= 20, arr[i-k]=arr[4-3=1]= 8
        #   window_sum = 33+(20)-(8) = 45. max_sum=45
        # loop3:
        #   arr[i]=arr[5]= 7, arr[i-k]=arr[5-3=2]= 30
        #   window_sum = 45+(7)-(30) = 22. max_sum=45
        # return max_sum=45
        window_sum = window_sum + arr[i] - arr[i - k]  # slide the window forward
        max_sum = max(max_sum, window_sum)
        print(f"window_sum2: {window_sum}, max_sum2: {max_sum}")

    return max_sum

# Example usage
arr = [1, 8, 30, -5, 20, 7]
k = 3
print(max_sum_subarray(arr, k))  # Output: 45

"""
Benefits of Sliding Window:

    Reduces time complexity from O(n×k)O(n×k) in naive approaches to O(n)O(n) by avoiding repeated summation.

    Efficient for problems requiring analysis of contiguous sequences in arrays or strings.

This technique can be adapted for variable window sizes or different conditions depending on the problem 
(e.g., longest substring without repeating characters, smallest window containing some characters) 
by adjusting the way the window expands and contracts.

In summary, the sliding window algorithm offers a systematic, efficient way to handle problems involving 
contiguous data ranges by maintaining a dynamically shifting subset and updating its state incrementally 
instead of recomputing from scratch.
"""