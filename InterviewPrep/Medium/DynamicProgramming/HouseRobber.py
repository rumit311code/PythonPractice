"""
https://neetcode.io/problems/house-robber

Video: https://www.youtube.com/watch?v=73r3KWiEvyk 7:10

House Robber

You are given an integer array nums where nums[i] represents the
amount of money the ith house has. The houses are arranged in a straight line,
i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses
because the security system will automatically alert the police
if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [1,1,3,3]
Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List

# use dynamic programming to calculate the max amount can be robbed at each index.

class Solution:
    def rob(self, nums: List[int]) -> int:
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