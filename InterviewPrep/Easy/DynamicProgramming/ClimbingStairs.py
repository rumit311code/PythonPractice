"""
https://neetcode.io/problems/climbing-stairs

Climbing Stairs

You are given an integer n representing the number of steps to reach the top of a staircase.
You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:
Input: n = 2
Output: 2
Explanation:
1 + 1 = 2
2 = 2

Example 2:
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3

Constraints:
1 <= n <= 30
"""

# Use binary decision tree
# for each step, add 1 and 2 and find out all the paths until all paths are visited.
# use depth first search where the left most path will have all the paths calculated
# that will occur in rest of the paths.

# bottom up approach -> solve for the last step.
# this will result in a Fibonacci pattern up to the number.

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one

"""
Runtime: O(n) -> covering depth upto the number, loop upto n-1.
Space: O(1) -> to store values one and two.
"""