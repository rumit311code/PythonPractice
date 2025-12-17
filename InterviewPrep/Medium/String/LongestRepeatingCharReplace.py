"""
https://neetcode.io/problems/longest-repeating-substring-with-replacement/question

Video: https://www.youtube.com/watch?v=gqXU1UyA8pk

Longest Repeating Character Replacement

You are given a string s consisting of only uppercase english characters and
an integer k. You can choose up to k characters of the string and replace
them with any other uppercase English character.

After performing at most k replacements, return the length of the
longest substring which contains only one distinct character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5

Constraints:

1 <= s.length <= 1000
0 <= k <= s.length
"""
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use sliding window technique
        #   start at the same (0) beginning for left and right -> first window.
        #   keep moving right pointer until the "condition" below is satisfied.
        # condition = window length - count[most freq char] -> gives the number of chars we need to replace
        #   this number <= k -> window is valid.
        #   if not, window is not valid for any replacement, increment left pointer.
        #   replace the character that is less frequent

        # s = "AAABABB", k = 1
        count = {}
        res = 0

        left = 0
        # max_f = 0
        for right in range(len(s)):
            # update char count dict
            count[s[right]] = count.get(s[right], 0) + 1
            # max_f = max(max_f, count[s[right]] - 1)

            # window validation
            # right - left + 1 -> window length
            # k -> num of replacements
            # max(count.values()) -> character with max repetitions.
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1 # reduce the count for the character.
                left += 1 # increment left pointer.

            res = max(res, right - left + 1)
        return res
Solution().characterReplacement("XYYX", 2)
"""
Runtime: O(26.n) -> O(n)
Space: O(n)
"""