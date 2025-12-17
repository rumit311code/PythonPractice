"""
https://neetcode.io/problems/search-for-word/question

Video: https://www.youtube.com/watch?v=pfiQ_PS1g8E

Word Search

Given a 2-D grid of characters board and a string word, return true
if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in
the board with horizontally or vertically neighboring cells.
The same cell may not be used more than once in a word.

Example 1:
Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"
Output: true

Example 2:
Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"
Output: false

Constraints:

1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i): # O(dfs)
            print(f"-----New dfs: r = {r}, c = {c}, i = {i}, path = {path}")
            if i == len(word): # found the full word match
                print(f"----- -----Found a match at {(r,c)}. returning True.")
                return True

            if( # invalid cases - match not found.
                    r < 0 or # row out of bound
                    c < 0 or # column out of bound
                    r >= rows or # row out of bound
                    c >= cols or # column out of bound
                    word[i] != board[r][c] or # character does match the current cell
                    (r,c) in path # cell already visited before
            ):
                print(f"----- ----- -----Invalid case. returning False.")
                return False

            path.add((r,c)) # found the character at r,c. valid case.
            print(f"----- ----- ----- -----Added {(r,c)} to path. Updated path = {path}")
            res = ( # search for the next character(i+1) in all 4 adjacent positions of (r,c).
                dfs(r + 1, c, i + 1) or # next row
                dfs(r - 1, c, i + 1) or # previous row
                dfs(r, c + 1, i + 1) or # next column
                dfs(r, c - 1, i + 1)    # previous column
            )

            print(f"----- ----- ----- ----- -----updated res = {res}")
            # When one path does not work out, need to remove all the visited positions
            # along this path, before exploring other possible paths in the next iteration.
            path.remove((r,c))
            print(f"----- ----- ----- ----- -----done visiting {(r,c)}. removed from path. Updated path = {path}")
            return res

        for r1 in range(rows): # O(n.m)
            for c1 in range(cols):
                print(f"Calling DFS at {(r1, c1)}.")
                if dfs(r1, c1, 0):
                    print(f"===== found a match at {(r1,c1)}. returning True.")
                    return True
                print(f"No match found at {(r1, c1)}.")
        return False

board1 = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word1 = "CAT"

board2 = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word2 = "BAT"

# print(Solution().exist(board1, word1))
print(Solution().exist(board2, word2))
"""
dfs = 4 branches ^ len(word) = 4^len(word)
Runtime: O(n.m.dfs) = 4^len(word)
Space: O(n) -> to store visited path.
"""