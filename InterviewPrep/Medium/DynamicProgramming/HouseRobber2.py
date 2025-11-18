"""
https://neetcode.io/problems/house-robber-ii

Video: https://www.youtube.com/watch?v=rWAJCfYYOvM 6:00

House Robber II

-> This is same as house robber1, except that first and last elements are adjacent.

You are given an integer array nums where nums[i] represents the amount of money the ith house has.
The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses
because the security system will automatically alert the police
if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [3,4,3]
Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List

# use dynamic programming to calculate the max amount can be robbed at each index.

class Solution:
    def rob(self, nums: List[int]) -> int:
        # max of all the houses except for first and last because first and last are adjacent.
        # nums[0] for the case where nums has only one element.
        return max(nums[0], self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        one_house_back, two_houses_back = 0, 0
        # [two_back, one_back, n, n+1, ...]
        # two_houses_back: previous to previous house
        # one_house_back: previous house
        # maintain just last 2 houses that you can rob
        #
        for n in nums: # O(n) loop
            temp = max(n + two_houses_back, one_house_back)
            two_houses_back = one_house_back
            one_house_back = temp
        return one_house_back

print(f"[2,9,8,3,6] ==> |{Solution().rob([2,9,8,3,6])}|")
print(f"[5,1,2,10,6,2,7,9,3,1] ==> |{Solution().rob([5,1,2,10,6,2,7,9,3,1])}|")

"""
Runtime: O(n) to loop nums
Space: O(1) to store the total
"""