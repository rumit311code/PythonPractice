"""
https://neetcode.io/problems/rotate-matrix/question

Video: https://www.youtube.com/watch?v=fMSJSS7eO1w

Rotate Image
Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [
  [1,2],
  [3,4]
]
Output: [
  [3,1],
  [4,2]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        [print(r) for r in matrix]
        left = 0
        right = len(matrix) - 1

        while left < right: # O(n)
            print(f"-----BEFORE: left: {left}, right: {right}")

            for i in range(right - left): # O(n)
                print(f"----- -----i:{i}")

                top, bottom = left, right

                # save top left value
                top_left = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left to top right
                matrix[top + i][right] = top_left

                print("----- -----updated matrix")
                [print(r) for r in matrix]

            left += 1
            right -= 1
            print(f"-----AFTER: left: {left}, right: {right}")

        print("===== ===== ROTATED MATRIX===== =====")
        [print(r) for r in matrix]

matrix1 = [
  [1,2],
  [3,4]
]
matrix2 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Solution().rotate(matrix1)
Solution().rotate(matrix2)