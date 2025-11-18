"""
https://neetcode.io/problems/two-integer-sum

Maximum Subarray

Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [2,-3,4,-2,2,1,-1,4]
Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:
Input: nums = [-1]
Output: -1

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

"""
from typing import List

# uses Kadane's Algorithm for the dynamic programming.
# anytime we get a negative prefix, reset the sum, shift right and start again.

class Solution:
    def max_sum_sub_array(self, nums: List[int]) -> int:
        res = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            res = max(res, cur_sum)
            print(f"res AFTER: {res}")
        return res

print(f"[2,-3,4,-2,2,1,-1,4] ==== |{Solution().max_sum_sub_array([2,-3,4,-10,-4,-1,-1,-4])}|")
print(f"[2,-3,4,-10,-4,-1,-1,-4] ==== |{Solution().max_sum_sub_array([2,-3,1,-10,-4,-1,-1,-4])}|")
print(f"[2,-3,4,-2,2,1,-1,4] ==== |{Solution().max_sum_sub_array([-2,-3,-4,-2,-2,-1,-1,-4])}|")
print(f"[-1] ==== |{Solution().max_sum_sub_array([-1])}|")
print(f"[-1, -2] ==== |{Solution().max_sum_sub_array([-1, -2, -3])}|")
print(f"[-1, -2] ==== |{Solution().max_sum_sub_array([-3, -1, -2])}|")
"""
Run time: O(n) as it iterates the loop only once.
Space: O(1) to store min and max values.
"""