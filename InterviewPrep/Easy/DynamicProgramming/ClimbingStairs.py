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

# Use binary decision tree - depth first search and recursion
# the nth step and n-1th step will always have 1 path because taking 2 steps will go out of bound.
# so initialize n = 1 and n-1 = 1
# from n-2 onwards, count the steps using Fibonacci pattern
# so (n-2) = (n-1) + n
# so for n = 5
# dp[5] = 1 -> n, base case
# dp[4] = 1 -> n-1, base case
# dp[3] = dp[4] + dp[5] = 2
# dp[2] = dp[3] + dp[4] = 3
# dp[1] = dp[2] + dp[3] = 5
# dp[0] = dp[1] + dp[2] = 8
# dp[0] is the total number of distinct ways to climb to the top of the staircase.
# this is O(n) because we're solving each sub problem (each step) only once.

# bottom up approach because 0th step depends on 1, 1 on 2 ....4 on 5.
class Solution:
    def climbStairs(self, n: int) -> int:
        N, N_1 = 1, 1
        # N = nth step = dp[5]
        # N_1 = (n-1)th step = dp[4]
        for _ in range(n-1): # n-1=4, so 0,1,2,3 -> total 4 loops + 2 base cases.
            tmp = N_1 # dp[4]
            N_1 = N_1 + N # new N_1 = dp[3] = dp[4] + dp[5] = 1 + 1 = 2
            N = tmp # new N = old N_1 = dp[4]
        return N_1 # this will be dp[0]

print(f"{Solution().climbStairs(5)}")
"""
Runtime: O(n) -> covering depth upto the number, loop upto n-1.
Space: O(1) -> to store values one and two.
"""