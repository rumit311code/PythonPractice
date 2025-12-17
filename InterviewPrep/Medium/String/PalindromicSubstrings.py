"""
https://neetcode.io/problems/palindromic-substrings/question

Video: https://www.youtube.com/watch?v=4RACzI5-du8

Palindromic Substrings

Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6

Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings
are counted as different palindromes even if the string contents are the same.

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        # for each character, check the longest palindrom it can have.
        # check left and right pointers until a mismatch is found.

        for i in range(len(s)): #O(n)

            # for odd length
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]: #O(n)
                res.append(s[left:right + 1])
                left -= 1  # move left pointer towards 0
                right += 1  # move right pointer towards len(s)

            # for even length
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]: #O(n)
                res.append(s[left:right + 1])
                left -= 1  # move left pointer towards 0
                right += 1  # move right pointer towards len(s)

        print(f"all palindromes: |{res}|")
        return len(res)

# Solution().countSubstrings(s="abc")
Solution().countSubstrings(s="aaa")

"""
Runtime: O(n) for loop * O(n) while loop = O(n2).
Space: O(n) to store result.
"""