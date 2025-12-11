"""
https://neetcode.io/problems/maximum-product-subarray

Video: https://youtu.be/lXVy6YWFcRM

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
#
class Solution:
    def max_product_sub_array(self, nums: List[int]) -> int:
        res = max(nums) # O(n)
        cur_min = 1
        cur_max = 1
        # [2,-3,0,-4]
        # cur_min=1, cur_max=1, res=4
        #
        # loop1: n=2 : cur_min=1,cur_max=2 (n=2 * cur_max=1 = 2), res=2(max num is 2)
        # loop2: n=-3: cur_min=1(no change) ,cur_max=2 (because of 2 * 1), res=2
        # loop3: n=0 : cur_min=1,cur_max=1 (reset cur_min and cur_max because n=0), res=2
        # loop4: n=-4: cur_min=-4(n=-4 * cur_min=1 = -4),cur_max=-4(n=-4 * cur_max=1 = -4), res=2
        # final answer = res = 2
        for n in nums: # O(n) loop
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

        # solution 2: O(nlogn)
        # sort first, take the last 2 elements.
        # nums.sort() # O(nlogn)
        # return max(nums[len(nums)-1], nums[len(nums)-1] * nums[len(nums)-2]) # O(1) - index access

# print(f"[2,-3,4,-2,2,1,-1,4] ==== |{Solution().max_product_sub_array([2,-3,4,-2,2,1,-1,4])}|")
# print(f"[2,-3,4,0,-4,0,-1,-4] ==== |{Solution().max_product_sub_array([2,-3,4,0,-4,0,-1,-4])}|")
# print(f"[-2, -1] ==== |{Solution().max_product_sub_array([-2, -1] )}|")
print(f"[2, -3, 0, -4] ==== |{Solution().max_product_sub_array([2, -3, 0, -4])}|")
"""
Sol1
Run time: O(n) to find max for res + O(n) to loop nums = O(n).
Space: O(1) to store min and max values.

Sol2 -> start with this and then check if improvement is needed in sol1.
Run time: O(nlong) for sorting + O(1) for getting last item + O(1) for getting 2nd last item 
Space: O(1) to update the sorted array in place.
"""