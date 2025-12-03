"""
https://neetcode.io/problems/count-paths/question

Video: https://www.youtube.com/watch?v=IlEsdxuD4lY

Unique Paths

There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Input: m = 3, n = 6
Output: 21
Example 2:

Input: m = 3, n = 3
Output: 6
Constraints:

1 <= m, n <= 100
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        print(f"m: {m}, n: {n}")

        dp = [[0] * n for _ in range(m)]
        [print(r) for r in dp]
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]

        # base case, set entire last row = 1
        dp[m-1] = [1] * n
        print(f"=====")
        [print(r) for r in dp]
        # [0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0, 0]
        # [1, 1, 1, 1, 1, 1, 1]

        # base case, set entire last column = 1
        # for i in range(m):
        #     dp[i][n-1] = 1
        [row.__setitem__(n-1, 1) for row in dp]
        print(f"=====")
        [print(r) for r in dp]
        # [0, 0, 0, 0, 0, 0, 1]
        # [0, 0, 0, 0, 0, 0, 1]
        # [1, 1, 1, 1, 1, 1, 1]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
                # dp[i+1][j] -> move down
                # dp[i][j+1] -> move right
                print(f"-----")
                [print(r) for r in dp]
        print(f"=====")
        [print(r) for r in dp]
        # [28, 21, 15, 10, 6, 3, 1]
        # [7, 6, 5, 4, 3, 2, 1]
        # [1, 1, 1, 1, 1, 1, 1]

        return dp[0][0]

print(f" 3,7 matrix: -> {Solution().uniquePaths(3, 7)}")
# print(f" 3,6 matrix: -> {Solution().uniquePaths(3, 6)}")
# print(f" 3,3 matrix: -> {Solution().uniquePaths(3, 3)}")

"""
Runtime: O(m*n)
Space: O(m*n)
"""

class Solution2:
    def uniquePaths2(self, m: int, n: int) -> int:
        print(f"m: {m}, n: {n}")

        row = [1] * n

        print("=====")
        print(row)

        for i in range(m-1):
            print(f" i: {i}")
            newRow = [1] * n
            print(f"row1====={row}====")
            print(f"newRow1=={newRow}====")
            for j in range(n-2, -1, -1):
                print(f"j: {j}")
                newRow[j] = row[j] + newRow[j+1]
                print(f"row2-----{newRow}-----")
            row = newRow
            print(f"newRow2--{row}-----")

        return row[0]

print(f" 3,7 matrix: -> {Solution2().uniquePaths2(3, 7)}")

"""
Runtime: O(m*n)
Space: O(n)
"""