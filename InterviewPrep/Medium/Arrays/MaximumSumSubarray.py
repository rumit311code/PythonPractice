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
# anytime we get a negative prefix, reset the sum, shift right and continue.

class Solution:
    def max_sum_sub_array(self, nums: List[int]) -> int:
        res = nums[0]
        cur_sum = 0

        # [2,-3,0,-4]
        # cur_sum=0, res=2
        #
        # loop1: n=2 : cur_sum=(n+cur_sum)=(2+0)=2, res=2
        # loop2: n=-3: cur_sum=(n+cur_sum)=(2-3)=-1, res=2
        # loop3: n=0 : reset cur_sum=0, cur_sum=(n+cur_sum)=(0+0)=0, res=2
        # loop4: n=-4: reset cur_sum=0, cur_sum=(n+cur_sum)=(-4+0)=-4, res=2
        #
        # final answer = res = 2
        for n in nums: # O(n) loop
            if cur_sum < 0:
                cur_sum = 0 # don't need negative sum as that will only reduce the sum.
            cur_sum += n # even for all negative numbers this will reset to the largest number.
            res = max(res, cur_sum)
            print(f"res AFTER: {res}")
        return res

        # solution 2: O(nlogn)
        # sort first, take the last 2 elements.
        # nums.sort() # O(nlogn)
        # return max(nums[len(nums)-1], nums[len(nums)-1] + nums[len(nums)-2]) # O(1) - index access

print(f"[2,-3,0,-4] ==== |{Solution().max_sum_sub_array([2,-3,0,-4])}|")
print(f"[-2,-3,-4] ==== |{Solution().max_sum_sub_array([-2,-3,-4])}|")
# print(f"[2,-3,4,-2,2,1,-1,4] ==== |{Solution().max_sum_sub_array([2,-3,4,-10,-4,-1,-1,-4])}|")
# print(f"[2,-3,4,-10,-4,-1,-1,-4] ==== |{Solution().max_sum_sub_array([2,-3,1,-10,-4,-1,-1,-4])}|")
# print(f"[2,-3,4,-2,2,1,-1,4] ==== |{Solution().max_sum_sub_array([-2,-3,-4,-2,-2,-1,-1,-4])}|")
# print(f"[-1] ==== |{Solution().max_sum_sub_array([-1])}|")
# print(f"[-1, -2] ==== |{Solution().max_sum_sub_array([-1, -2, -3])}|")
# print(f"[-1, -2] ==== |{Solution().max_sum_sub_array([-3, -1, -2])}|")
"""
Sol1
Run time: O(n) as it iterates the loop only once.
Space: O(1) to store min and max values.

Sol2 -> start with this and then check if improvement is needed in sol1.
Run time: O(nlong) for sorting + O(1) for getting last item + O(1) for getting 2nd last item 
Space: O(1) to update the sorted array in place.
"""