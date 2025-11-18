"""
https://neetcode.io/problems/find-minimum-in-rotated-sorted-array

Find Minimum in Rotated Sorted Array

You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning.
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2]
Output: 1

Example 2:
Input: nums = [4,5,0,1,2,3]
Output: 0

Example 3:
Input: nums = [4,5,6,7]
Output: 4

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

"""
from typing import List

# binary search
# if left most is smaller than right most -> array is sorted -> return the first element.
# if rotated array
#   if middle element >= left most
#       middle is in left sorted array -> search right side.
#           otherwise
#       middle is in right sorted array -> search left side.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]: # array is already sorted.
                res = min(res, nums[l]) # get the min of current res or left most.
                break

            # // (Double forward slash): This performs "floor division" or "integer division."
            # It returns the integer part of the quotient, rounded down to the nearest whole number.
            m = (l+r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1 # search right side.
            else:
                r = m - 1 # search left side.
        return res
"""
Run time: O(n logn) because of binary search.
Space: O(1) to store the result and min, l and m.
"""