"""
https://neetcode.io/problems/count-number-of-islands/question

Video: https://www.youtube.com/watch?v=pV2kpPD66nE

Number of Islands

Given a 2D grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.
You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Example 2:
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4

Constraints:

1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.
"""
import collections

grid1 = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

grid2 = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
class Solution: # BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        # total rows and columns to explore.
        rows, cols = len(grid), len(grid[0])

        # explore all adjacent cells (Left, Right, Up and Down) of a cell.
        paths = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def explore(row, column):
            print(f"----- ----- exploring cell: {(row, column)}")
            if (
                    row < 0 or # if row out of bound
                    row >= rows or # if row out of bound
                    column < 0 or # if column out of bound
                    column >= cols or # if column out of bound
                    grid[row][column] == '0' # if cell is NOT an island
            ):
                print(f"----- ----- ----- found a non-island cell {(row, column)}")
                return 0

            grid[row][column] = '0' # set the visited island to 0 so that it's not visited again.
            print(f"----- ----- ----- marked cell {(row, column)} as 0")
            for a, b in paths:
                print(f"----- ----- ----- adjacent cell: {(a, b)}")
                explore(row + a, column + b)

            print(f"----- ----- ----- ----- returning 1 for cell {(row, column)}")
            return 1

        islands = 0
        for i in range(rows):
            for j in range(cols):
                print(f"----- current cell: {(i, j)}")
                islands += explore(i, j)
        return islands

print(f"Total islands for grid1: {Solution().numIslands(grid1)}")
print(f"Total islands for grid2: {Solution().numIslands(grid2)}")

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c): # breadth-first-search is iterative
            print("----- New BFS -----")
            print(f"-----r2: {(r,c)}")
            print(f"-----visited2: {visited}")
            print("----- ----- -----")

            q = collections.deque() # queue is used for BFS usually.
            visited.add((r,c))
            print(f"-----visited3: {visited}")
            q.append((r,c)) # update the queue
            print(f"-----q1: {q}")

            while q:
                print("----- ----- -----")
                print("----- New while loop -----")
                print("----- ----- -----")

                print(f"----- -----q2: {q}")
                row, col = q.popleft() # popleft for breadth first search.
                # row, col = q.pop() # use pop() for depth first search - iterative.
                print(f"----- -----row: {(row, col)}")
                print(f"----- -----q3: {q}")

                # 1,0  -> down
                # -1,0 -> up
                # 0,1  -> right
                # 0,-1 -> left
                directions = [(1,0),(-1,0),(0,1),(0,-1)]

                for dr, dc in directions:
                    r1, c1 = row + dr, col + dc
                    print(f"----- ----- -----r3: {(r1,c1)}")
                    if(
                            r1 in range(rows) and # row is in bound
                            c1 in range(cols) and # column is in bound
                            grid[r1][c1] == "1" and # cell is an island
                            (r1, c1) not in visited # cell is not visited before
                    ):
                        q.append((r1, c1)) # update the queue
                        print(f"----- ----- ----- -----q4: {q}")
                        visited.add((r1, c1))  # update the visited list
                        print(f"----- ----- ----- -----visited4: {visited}")

        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    print("=====  NEW ISLAND CELL START  =====")
                    print(f"r1: {(r,c)}")
                    print(f"visited1: {visited}")
                    print("===== ===== ===== ===== ===== =====")
                    bfs(r, c)
                    islands += 1
        return islands
# print(Solution2().numIslands(grid))

# class Solution3: # DFS DID NOT WORK
#     def numIslands(self, grid: List[List[str]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#
#         def dfs(r, c):
#             if r < 0 or c < 0 or r >= rows or c >= cols:
#                 return
#             if grid[r][c] != '1':
#                 return
#
#             grid[r][c] = '0'
#             dfs(i - 1, j)
#             dfs(i, j + 1)
#             dfs(i + 1, j)
#             dfs(i, j - 1)
#
#         islands = 0
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == '1':
#                     islands += 1
#                     dfs(i, j)  # Or use bfs(i, j)
#         return islands
#
# print(Solution3().numIslands(grid))