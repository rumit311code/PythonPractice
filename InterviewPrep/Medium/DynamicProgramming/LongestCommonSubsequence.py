"""
https://neetcode.io/problems/longest-common-subsequence

Longest Common Subsequence

Video: https://www.youtube.com/watch?v=Ua0GhsJSlWM

Given two strings text1 and text2, return the length of the
longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence
by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:
Input: text1 = "cat", text2 = "crabt"
Output: 3
Explanation: The longest common subsequence is "cat" which has a length of 3.

Example 2:
Input: text1 = "abcd", text2 = "abcd"
Output: 4

Example 3:
Input: text1 = "abcd", text2 = "efgh"
Output: 0

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

# recursive: if first chars are equal find lcs of remaining of each,
# else max of: lcs of first and remain of 2nd and lcs of 2nd remain of first, cache result;
# nested forloop to compute the cache without recursion;
#
# depth search: bottom up (start at last index and end at first) approach
# create a matrix of (i+1 x j+1) size -> i(len string1), j (len string2)
#   the last row and column are for empty strings (no matches)
#   because (i+1, j+1) are for empty strings, cell values will be 0
#
# fill out the matrix
# create a matrix of (i+1 x j+1)
#   set all last row and last column values to 0
# start loop from (i+1, j+1) and iterate up to the beginning of the matrix (0,0)
#   if characters match
#       1 + (value at diagonal cell) -> this is a match of the character
#   if characters don't match
#       0 + max(i+1(right), j+1(bottom))
#   repeat
# the answer will be the value in the top-left (0,0) cell.
# final matrix below for reference for "crabt" and "cat"
#
#    c  a  t
# c [3, 2, 1, 0]
# r [2, 2, 1, 0]
# a [2, 2, 1, 0]
# b [1, 1, 1, 0]
# t [1, 1, 1, 0]
#   [0, 0, 0, 0]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        # [0, 0, 0, 0]
        # [0, 0, 0, 0]
        # [0, 0, 0, 0]
        # [0, 0, 0, 0]
        # [0, 0, 0, 0]
        # [0, 0, 0, 0]
        # all cell values set to 0 to start with

        [print(r) for r in dp]

        for i in range(len(text1) - 1, -1, -1): # First O(n) loop
            for j in range(len(text2) - 1, -1, -1): # Second O(n) loop
                if text1[i] == text2[j]: # characters match
                    dp[i][j] = 1 + dp[i+1][j+1] # 1 + diagonal cell value
                else: # characters don't match
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    # max of right cell(dp[i][j+1]) or bottom cell(dp[i+1][j])
                print(f"==========")
                [print(r) for r in dp]
        return dp[0][0] # return top-left cell value.

print(f"(crabt, cat): {Solution().longestCommonSubsequence("crabt","cat")}")


"""
Runtime: O(len(text1) * len(text2)) -> two nested O(n) loops for matrix traversal.
Space: O(n^2) -> 2d matrix storage.
"""