"""
https://neetcode.io/problems/decode-ways

Video: https://www.youtube.com/watch?v=6aEyTjOwlJU

Decode Ways

A string consisting of uppercase english characters can be encoded
to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into
letters using the reverse of the mapping above. There may be multiple ways
to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter
since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it.
You can assume that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "01"
Output: 0
Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

Constraints:

1 <= s.length <= 100
s consists of digits
"""

# WATCH VIDEO AGAIN.

### Case 1: `dp[i] = dp[i+1]`

# If the digit at `i` can *only* stand alone (like `6` in `"671"`),
# then the only choice is to decode that digit and move on.
# So the number of ways = whatever ways exist from `i+1`.

# Example: `"671"`
# - The `"6"` cannot combine with `"7"` (since `"67"` is invalid).
# - So the only option is `(6)(71)`.
# - That’s why `dp[i] = dp[i+1]`.

### Case 2: `dp[i] = dp[i+1] + dp[i+2]`

# If the digit at `i` can *either* stand alone *or*
# combine with the next digit to make a valid two-digit code, then there are two choices:
# 1. Decode it alone → gives you `dp[i+1]`.
# 2. Decode it together with the next digit → gives you `dp[i+2]`.

# Example: `"2671"`
# - At `"2"`, you can take it alone → `(2)(671)`, that’s `dp[i+1]`.
# - Or combine `"2"` and `"6"` → `(26)(71)`, that’s `dp[i+2]`.
# - Total ways = `dp[i+1] + dp[i+2]`.

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        print(f"dp1: {dp}")

        def dfs(i):
            # print(f"i1: {i}")
            if i in dp:
                return dp[i]
            # print(f"s[i]1: {s[i]}")
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            # print(f"i2: {i}, i+1: {i+1},")
            # print(f"res1: {res}")
            if(i+1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i+1] in "0123456")):
                # print(f"s[i]2: {s[i]}, s[i+1]: {s[i+1]}, s[i+2]: {s[i+2]}")
                res += dfs(i+2)
                # print(f"res2: {res}")
            # print(f"res3: {res}")
            dp[i] = res
            # print(f"dp2: {dp}")
            return res
        return dfs(0)

print(Solution().numDecodings("121"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
"""
Runtime: O(n)
Space: O(1)
"""