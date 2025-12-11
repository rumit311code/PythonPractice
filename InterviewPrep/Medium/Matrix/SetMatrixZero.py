"""
https://neetcode.io/problems/set-zeroes-in-matrix/question

Video: https://www.youtube.com/watch?v=T41rL0L3Pnw

Set Matrix Zeroes

Given an m x n matrix of integers matrix,
if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:
Input: matrix = [
  [0,1],
  [1,0]
]
Output: [
  [0,0],
  [0,0]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]

Constraints:
1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1
"""
class Solution: # O(n*m)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        [print(r) for r in matrix]
        rows, cols = len(matrix), len(matrix[0])
        # first row to mark which row should be set to zero.
        # first column to mark which columns should be set to zero.

        # assume that first row will not be set to zero.
        row_zero = False

        # determine which rows/cols need to be zero in the first row and column.
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0: # current cell is 0.

                    # mark [row0, col] to zero.
                    # To be used to set all rows to zero in this column later.
                    matrix[0][c] = 0

                    # first row zero out flag is stored in row_zero
                    # update this flag only from 2nd row onwards.
                    if r > 0:
                        # mark [row, col0] to zero.
                        # To be used to set all columns to zero in this row later.
                        matrix[r][0] = 0
                    else: # r=0
                        row_zero = True # update the first row as 0 based on this flag.

        # zero out every cell except for first row and column.
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # first column zero out.
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # first row zero out.
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        [print(r) for r in matrix]

matrix1 = [
  [0,1],
  [1,0]
]
matrix2 = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
matrix3=[
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
Solution().setZeroes(matrix1)
Solution().setZeroes(matrix2)
Solution().setZeroes(matrix3)

"""
m = rows, n = cols
Runtime: (m.n) to iterate over the matrix, fill out rows array and fill columns array.
Space: O(m+n) to create 2 arrays.
"""