"""
https://neetcode.io/problems/longest-palindromic-substring/question

Video: https://www.youtube.com/watch?v=XYQecbcd6_c

Longest Palindromic Substring

Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length,
return any one of them.

Example 1:
Input: s = "ababd"
Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:
Input: s = "abbc"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s contains only digits and English letters.
"""


class Solution:
    res = ""
    res_len = 0

    def get_longest_palindrome(self, s, left, right):

        print(f"-----left:{left}, right:{right}, res:{Solution.res}, res_len:{Solution.res_len}")
        while left >= 0 and right < len(s) and s[left] == s[right]: #O(n)
            print(f"----- -----Same char |{s[left]}| found at left and right.")
            # check if the current sequence longer than the previous one and update if it is.
            if right - left + 1 > Solution.res_len:
                print(f"----- ----- -----current seq longer than prev.")
                # this is the longest sequence. This is optional and can be skipped if not asked.
                # this is O(n) operation in worst case and will make the solution O(n3). So, instead do brute force.
                Solution.res = s[left:right + 1]

                # change the new longest length.
                Solution.res_len = right - left + 1
                print(f"----- ----- -----updated longest seq: left:{left}, right:{right}, res:{Solution.res}, res_len:{Solution.res_len}")
            left -= 1  # move left pointer towards 0
            right += 1  # move right pointer towards len(s)
            print(f"----- ----- ----- -----NEW left:{left}, right:{right}")

    def longestPalindrome(self, s: str) -> str:
        # for each character, check the longest palindrom it can have.
        # check left and right pointers until a mismatch is found.

        for i in range(len(s)): #O(n)
            # odd length: i=0,1,2,3,4
            # ababd
            # left, right = i, i
            print(f"i:{i}: running for ODD")
            self.get_longest_palindrome(s=s, left=i, right=i)

            # even length: i=0,1,2,3
            # abbc, aa
            # left, right = i, i + 1
            print(f"i:{i}: running for EVEN")
            self.get_longest_palindrome(s=s, left=i, right=i + 1)

        return Solution.res

Solution().longestPalindrome(s="ababd")

"""
Runtime: O(n) for loop * O(n) while loop = O(n2).
Space: O(n) to store result.
"""