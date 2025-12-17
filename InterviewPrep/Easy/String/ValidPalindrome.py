"""
https://neetcode.io/problems/is-palindrome/question

https://www.youtube.com/watch?v=jJXJ16kPFWg

Valid Palindrome

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""
import re

class Solution1: # O(n) runtime, O(n) space.
    def isPalindrome(self, s: str) -> bool:
        # [^a-zA-Z0-9]: pattern to match everything other than alphanumeric characters.
        # re.sub: replace all non-alphanumeric characters to empty string.
        # .lower() -> converts string to all lowercase (case-insensitive).
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # O(n)

        # s[::-1] -> reverses a string.
        return s == s[::-1] # O(n)

class Solution2: #O(logn) runtime, O(1) space.
    def isPalindrome(self, s: str) -> bool:
        # two pointer solution
        left = 0
        right = len(s)-1

        while left < right: # O(n)
            # both while loops below ignore non-alpha numeric characters.
            while left < right and not self.is_alpha_num(s[left]):
                left += 1
            while right > left and not self.is_alpha_num(s[right]):
                right -= 1

            # characters don't match, return False immediately.
            if s[left].lower() != s[right].lower():
                return False

            # move the pointers towards middle.
            left += 1
            right -= 1
        # all characters match fine. Return True.
        return True

    def is_alpha_num(self, c):
        return (
                ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9")
        )



"""
Runtime: O(n) for replace + O(n) for lower() + O(n) for reverse = 3.O(n) = O(n)
Space: Same as Runtime.
"""
print(Solution1().isPalindrome("Was it a car or a cat I saw?"))
print(Solution2().isPalindrome("Was it a car or a cat I saw?"))

