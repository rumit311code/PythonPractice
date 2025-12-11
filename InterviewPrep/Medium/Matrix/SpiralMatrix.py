"""
https://neetcode.io/problems/spiral-matrix/question

Video: https://www.youtube.com/watch?v=BJnMZNwUk1M

Spiral Matrix

Given an m x n matrix of integers matrix,
return a list of all elements within the matrix in spiral order.

Example 1:
Input: matrix = [
[1,2],
[3,4]
]
Output: [1,2,4,3]

Example 2:
Input: matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 3:
Input: matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0 # left boundary
        right = len(matrix[0]) # right boundary
        top = 0 # top boundary
        bottom = len(matrix) # bottom boundary

        while left < right and top < bottom:
            # Left -> Right : get every column in the TOP row
            for col in range(left, right):
                res.append(matrix[top][col])
            top += 1 # shift down for the top boundary

            # Top -> Bottom : get every row in the RIGHT column
            for row in range(top, bottom):
                res.append(matrix[row][right - 1])
            right -= 1 # shift left for the right boundary

            # to handle one row-multi column OR one column-multi row types matrix.
            # break out early if the boundaries crossed already.
            if not (left < right and top < bottom):
                break

            # Right -> Left : get every column in the BOTTOM row
            for col in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][col])
            bottom -= 1 # shift up for the bottom boundary

            # Bottom -> Top : get every row in the LEFT column
            for row in range(bottom - 1, top - 1, -1):
                res.append(matrix[row][left])
            left += 1 # shift right for the left boundary

        return res

matrix1 = [
    [1,2],
    [3,4]
]

matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix3 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(Solution().spiralOrder(matrix1))
print(Solution().spiralOrder(matrix2))
print(Solution().spiralOrder(matrix3))
"""
m: rows, n: cols
Runtime: O(m . n)
Space: O(1) for res variable
"""