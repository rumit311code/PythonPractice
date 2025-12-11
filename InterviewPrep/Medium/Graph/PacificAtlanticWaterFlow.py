"""
https://neetcode.io/problems/pacific-atlantic-water-flow/question

Video: https://www.youtube.com/watch?v=s-VkcjHqkGI

Pacific Atlantic Water Flow

You are given a rectangular island heights where heights[r][c] represents
the height above sea level of the cell at coordinate (r, c).

The islands border the Pacific Ocean from the top and left sides,
and border the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a
neighboring cell with height equal or lower.
Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans.
Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell.
You may return the answer in any order.

Example 1:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:
Input: heights = [
    [1],
    [1]
]
Output: [[0,0],[0,1]]

Constraints:

1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        print(f"pac = {pac}, atl = {atl}")
        def dfs(r, c, visit, cell_height):
            print(f"#### #### DFS #### ####")
            print(f"r = {r}, c = {c}, visit = {visit}, cell_height = {cell_height}")
            if(
                (r, c) in visit or
                r < 0 or
                c < 0 or
                r == ROWS or
                c == COLS or
                heights[r][c] < cell_height
            ):
                print("~~~~~ RETURN ~~~~~")
                return

            print(f"~~~~~ Adding visit {(r, c)}~~~~~")
            visit.add((r, c))

            print(f"----- ----- UP ----- -----")
            dfs(r - 1, c, visit, heights[r][c]) # up
            print(f"r = {r}, c = {c}, visit = {visit}, cell_height = {cell_height}")

            print(f"----- ----- DOWN ----- -----")
            dfs(r + 1, c, visit, heights[r][c]) # down
            print(f"r = {r}, c = {c}, visit = {visit}, cell_height = {cell_height}")

            print(f"----- ----- LEFT ----- -----")
            dfs(r, c - 1, visit, heights[r][c]) # left
            print(f"r = {r}, c = {c}, visit = {visit}, cell_height = {cell_height}")

            print(f"----- ----- RIGHT ----- -----")
            dfs(r, c + 1, visit, heights[r][c]) # right
            print(f"r = {r}, c = {c}, visit = {visit}, cell_height = {cell_height}")

        for c in range(COLS): # O(columns)
            dfs(0, c, pac, heights[0][c]) # first row
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # last row

        for r in range(ROWS): # O(rows)
            dfs(r, 0, pac, heights[r][0]) # first column
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # last column

        res = []
        for r in range(ROWS): # O(rows)
            for c in range(COLS): # O(columns) -> O(rows * columns)
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

print(Solution().pacificAtlantic([
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]))

print(Solution().pacificAtlantic([
    [1],
    [1]
]))