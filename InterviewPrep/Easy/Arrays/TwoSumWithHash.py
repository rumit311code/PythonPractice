"""
https://neetcode.io/problems/two-integer-sum

Two Sum

Given an array of integers nums and an integer target, return the indices i and j such that
nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000

"""
from typing import List

class Solution: # No need to create a class
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val: index
        for i, val in enumerate(nums): # using enumerate so that index and value can be accessed simultaneously.
            diff  = target - val
            if diff in prevMap:
                return [prevMap[diff], i] # the matching number with target diff found.
            prevMap[val] = i # keep adding non-matches

            # if j not in res:
            #     res[v] = i # if not, add the value and index.
            # else:
            #     output.extend([res.get(j), i])
            #     break # dont break if all pairs need to be found
        return [] # no pair found

nums = [5,5,8,10,0,6,8]
target = 10
pair = Solution().two_sum(nums, target)
print(f"the matching indexes of digits for target sum is |{pair[0]}==={pair[1]}|")
print(f"the matching values of digits for target sum is |{nums[pair[0]]}==={nums[pair[1]]}|")

"""
Run time: O(n) because iterating the array once.
Space: O(n) because using hashmap to store the array index on values.
"""