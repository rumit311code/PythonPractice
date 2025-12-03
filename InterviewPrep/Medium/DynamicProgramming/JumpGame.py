"""
https://neetcode.io/problems/jump-game/question

Video: https://www.youtube.com/watch?v=Yan0cv2cLy8

Jump Game

You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.

Example 1:
Input: nums = [1,2,0,1,0]
Output: true
Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

Example 2:
Input: nums = [1,2,1,0,1]
Output: false

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums = [3,2,1,0,4] -> False
        # nums = [1,2,0,1,0] -> True

        goal = len(nums) - 1 # set to 4
        print(nums)
        for i in range(len(nums) - 1, -1, -1): # O(n) loop [4,3,2,1,0]
            # Example1: nums = [3,2,1,0,4] -> False
            # i = 4: 4 + 1 >= 4 -> True -> new goal = i = 4
            # i = 3: 3 + 0 >= 4 -> False -> no change to goal, goal = 4
            # i = 2: 2 + 1 >= 4 -> False -> no change to goal, goal = 4
            # i = 1: 1 + 2 >= 4 -> False -> no change to goal, goal = 4
            # i = 0: 0 + 1 >= 4 -> False -> no change to goal, goal = 4
            # goal !=0 -> so False.
            #
            # Example2: nums = [1,2,0,1,0] -> True
            # i = 4: 4 + 0 >= 4 -> True -> new goal = i = 4
            # i = 3: 3 + 1 >= 4 -> True -> new goal = i = 3
            # i = 2: 2 + 0 >= 3 -> False -> no change to goal, goal = 3
            # i = 1: 1 + 2 >= 3 -> True -> new goal = i = 1
            # i = 0: 1 + 1 >= 1 -> True -> new goal = i = 0
            # goal=0 -> so True.

            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([1,2,1,0,1]))
print(Solution().canJump([1]))
print(Solution().canJump([0]))
print(Solution().canJump([2,0]))

"""
Runtime: O(n) to iterate the nums once.
Space: O(1) to store goal.
"""