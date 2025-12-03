"""
https://neetcode.io/problems/duplicate-integer

Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
"""
from collections import Counter
# iterate the array, and check if an element exists in the hashset. if yes, found a dup, if not, add it to hashset.

from typing import List

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        # Solution1: using hashset
        # use this if only True/False needed on the first occurrence.
        # hashset = set()
        #
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False

        # Solution2: using counter
        # use this if all dups needed.
        # occurrence_count = Counter(nums)
        return True if [k for k, v in Counter(nums).items() if v > 1] else False


print(f"contains dup |{Solution().contains_duplicate([1, 2, 3, 3])}|")
print(f"contains dup |{Solution().contains_duplicate([1, 2, 3])}|")
"""
with sorting + checking neighbors
Run time: O(nlogn) because need logn for sorting + n for iterating array
Space: O(1) for comparing 2 neighbours

without sorting + using hash set
Run time: O(n) -> O(1) for checking in set + O(1) to add the element to the set + O(n) for iterating array
Space: O(n) for storing hash set
"""