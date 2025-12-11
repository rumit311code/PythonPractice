"""
https://neetcode.io/problems/find-target-in-rotated-sorted-array

Video: https://youtu.be/U8XENwh8Oy8

Search in Rotated Sorted Array

You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target,
return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2], target = 1
Output: 4

Example 2:
Input: nums = [3,5,6,0,1,2], target = 4
Output: -1

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
All values of nums are unique.
nums is an ascending array that is possibly rotated.
"""
from typing import List

# binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            # // (Double forward slash): This performs "floor division" or "integer division."
            # It returns the integer part of the quotient, rounded down to the nearest whole number.
            m = (l + r) // 2
            print(f"l-m-r === |{l}|{m}|{r}|")
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]: # m is in left sorted array
                print(f"IF 1")
                if target > nums[m] or target < nums[l]: # target is on the right side of the middle
                    print(f"IF 1B")
                    l = m +1
                    continue
                elif target >= nums[l]: # target is on the left side of the middle
                    print(f"IF 1B")
                    r = m -1
                    continue
            else: # m is in right sorted array
                print(f"IF 2")
                if target < nums[m] or target > nums[r]: # target is on the left side of the middle
                    print(f"IF 2A")
                    r = m -1
                    continue
                elif target <= nums[r]:  # target is on the right side of the middle
                    print(f"IF 2B")
                    l = m +1
                    continue
        return -1

print(f"[3,5,6,0,1,2] ==== |{Solution().search([3,5,6,0,1,2],0)}|")
print(f"[0,1,2,3,5,6] ==== |{Solution().search([0,1,2,3,5,6],0)}|")
print(f"[3,5,6,0,1,2] ==== |{Solution().search([3,5,6,0,1,2],8)}|")
print(f"[0,1,2,3,5,6] ==== |{Solution().search([0,1,2,3,5,6],8)}|")
print(f"[1,3] ==== |{Solution().search([1,3],3)}|")
print(f"[1,3] ==== |{Solution().search([1,3],4)}|")
print(f"[1] ==== |{Solution().search([1],1)}|")
print(f"[1] ==== |{Solution().search([1],3)}|")
"""
Run time: O(logn) because of binary search.
Space: O(1) to store the result and min, l and m.
"""