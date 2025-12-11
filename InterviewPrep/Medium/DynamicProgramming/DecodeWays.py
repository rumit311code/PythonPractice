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
from typing import List, Any


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
# 26

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1} # {0:1, 1:1, 2:1}
        print(f"dp1: {dp}")

        def dfs(i):
            print(f"i1: {i}")
            if i in dp:
                return dp[i]

            print(f"s[i]1: {s[i]}")
            if s[i] == "0":
                return 0

            print(f"BEFORE DFS1: dp: {dp}")
            res = dfs(i+1)
            print(f"AFTER DFS1: res: {res}, dp: {dp}")
            if(
                    i+1 < len(s) and
                    (s[i] in "12" and s[i+1] in "0123456")
                ):
                print(f"s[i]2: {s[i]}, s[i+1]: {s[i+1]}")
                print(f"BEFORE DFS2: dp: {dp}")
                res += dfs(i+2)
                print(f"AFTER DFS2: res: {res}, dp: {dp}")
            print(f"AFTER both DFF1: res: {res}, dp: {dp}")
            print(f"i2: {i}")
            dp[i] = res
            print(f"AFTER both DFS2: res: {res}, dp: {dp}")
            return res
        return dfs(0)

# 671 -> 1 -> one -> [(6,7,1)]
# 1012 -> 2 -> two -> [(10,1,2),(10,12)]
# 2671 -> 2 -> two -> [(26,7,1),(2,6,7,1)]
print(Solution().numDecodings("671"))
# print(Solution().numDecodings("1012"))
# print(Solution().numDecodings("2671"))
"""
Runtime: O(n)
Space: O(1)
"""
class Solution2:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # {0:1, 1:1, 2:1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if(
                    i+1 < len(s) and
                    (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))
            ):
                dp[i] = dp[i] + dp[i+2]
        return dp[0]
"""
Runtime: O(n)
Space: O(n)
"""
# print(Solution2().numDecodings("671"))
# print(Solution2().numDecodings("1012"))
# print(Solution2().numDecodings("2671"))

class Solution3: #  DOES NOT WORK
    def numDecodings(self, s: str) -> List[Any]:
        # 671 -> 1 -> one-> [(6,7,1)]
        # 1012 -> 2 -> two -> [(10,1,2),(10,12)]
        # 2671 -> 2 -> two -> [(26,7,1),(2,6,7,1)]
        total_ways1 = []
        total_ways2 = []
        # total_ways3 = []
        print("===== =====")
        i=0
        while i < len(s):
            print(f"i:{i}, s[i]:{s[i]}, s[i+1]:{s[i+1] if (i+1) < len(s) else None}")
            print(f"total_ways1 START:{total_ways1}")
            print(f"total_ways2 START:{total_ways2}")
            if s[i] == "0": # i=0, cannot take 0 as a prefix
                print("^^^^^ ^^^^^")
                i += 1
                continue

            if i == len(s)-1:
                print("----- -----")
                if s[i] not in total_ways1:
                    total_ways1.extend([s[i]])
                if s[i] not in total_ways2:
                    total_ways2.extend([s[i]])
                print(f"total_ways1 1:{total_ways1}")
                print(f"total_ways2 1:{total_ways2}")
                i += 1
                continue

            if s[i] in "12":
                print("~~~~~ ~~~~~")
                if i+1 < len(s):
                    print("***** *****")
                    if s[i+1] == "0":
                        if s[i] + s[i+1] not in total_ways1: # 10, 20
                            total_ways1.extend([s[i] + s[i+1]])
                        if s[i] + s[i+1] not in total_ways2:
                            total_ways2.extend([s[i] + s[i+1]])
                        print(f"total_ways1 2:{total_ways1}")
                        print(f"total_ways2 2:{total_ways2}")
                        i += 2
                        continue
                    elif (s[i] == "1" or (s[i] == "2" and s[i+1] in "123456")): # (i=1 or 2) AND i+1=0123456
                        # if s[i] + s[i+1] not in total_ways1: # 12,26
                        #     total_ways1.extend([s[i] + s[i+1]])
                        # if s[i] + s[i+1] not in total_ways2:
                        #     total_ways2.extend([s[i] + s[i+1]])

                        if s[i] + s[i+1] not in total_ways1: # 10, 20
                            total_ways1.extend([s[i] + s[i+1]])
                        if s[i] + s[i+1] not in total_ways2:
                            total_ways2.extend([s[i] + s[i+1]])

                        if s[i] not in total_ways1: # 1 | 2
                            total_ways1.extend([s[i]])
                        if s[i+1] not in total_ways2: # 2 | 6
                            total_ways1.extend([s[i+1]])
                        print(f"total_ways1 3:{total_ways1}")
                        print(f"total_ways2 3:{total_ways2}")
            elif s[i] in "3456789":
                if s[i] not in total_ways1:
                    total_ways1.extend([s[i]])
                if s[i] not in total_ways2:
                    total_ways2.extend([s[i]])
                print(f"total_ways1 4:{total_ways1}")
                print(f"total_ways2 4:{total_ways2}")
            i += 1

            print(f"total_ways1 END:{total_ways1}")
            print(f"total_ways2 END:{total_ways2}")
            print("----- -----")
        return total_ways1 + total_ways2
# print(Solution3().numDecodings("671"))
# print(Solution3().numDecodings("1012"))
# print(Solution3().numDecodings("2671"))