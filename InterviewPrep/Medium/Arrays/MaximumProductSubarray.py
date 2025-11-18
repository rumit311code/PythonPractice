"""
https://neetcode.io/problems/maximum-product-subarray

Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Example 1:
Input: nums = [1,2,-3,4]
Output: 4

Example 2:
Input: nums = [-2,-1]
Output: 2

Constraints:

1 <= nums.length <= 1000
-10 <= nums[i] <= 10


"""
from typing import List

# uses Kadane's Algorithm for the dynamic programming.
# keep max and min product value and keep comparing with the next element.

class Solution:
    def max_product_sub_array(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min = 1
        cur_max = 1

        for n in nums:
            print("===================")
            print(f"cur_max: {cur_max}, cur_min: {cur_min}, res: {res}")
            if n == 0:
                cur_min = 1
                cur_max = 1
                continue
            tmp = n * cur_max
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)
            print(f"cur_max2: {cur_max}, cur_min2: {cur_min}, res2: {res}")
        return res

# print(f"[2,-3,4,-2,2,1,-1,4] ==== |{Solution().max_product_sub_array([2,-3,4,-2,2,1,-1,4])}|")
# print(f"[2,-3,4,0,-4,0,-1,-4] ==== |{Solution().max_product_sub_array([2,-3,4,0,-4,0,-1,-4])}|")
# print(f"[-2, -1] ==== |{Solution().max_product_sub_array([-2, -1] )}|")
print(f"[1, 2, -3, 4] ==== |{Solution().max_product_sub_array([1, 2, -3, 4])}|")
"""
Run time: O(n) as it iterates the loop only once.
Space: O(1) to store min and max values.
"""