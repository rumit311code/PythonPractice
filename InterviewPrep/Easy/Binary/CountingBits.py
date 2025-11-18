"""
https://neetcode.io/problems/counting-bits

Counting Bits

Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 4
Output: [0,1,1,2,1]

Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100

Constraints:

0 <= n <= 1000
"""
from typing import List


class Solution:
    # this is same problem as Number of One Bits, just in a loop.
    def countBits(self, n: int) -> List:
        # Solution 1: O(nlogn) Bruteforce
        # res = {}
        # for i in range(0,n+1): # O(n)
        #     count = 0
        #     cur = i
        #     while cur: # O(logn)
        #         count += cur % 2 # return 1 if the right most bit is 1 else 0.
        #         cur = cur >> 1
        #     res[i] = count
        # return res

        # Solution 2: O(n) Utilize previously calculated counts for 0 to 3 and use them for the numbers 4 onwards.
        # Bits in binary are doubling in the power of 2.
        # 0: 0000 -> 0
        # 1: 0001 -> 1 -> 1 + dp[n-1]
        # 2: 0010 -> 1 -> 1 + dp[n-2]
        # 3: 0011 -> 2 -> 1 + dp[n-2]
        # 4: 0100 -> 1 -> 1 + dp[n-4]
        # 5: 0101 -> 2 -> 1 + dp[n-4]
        # 6: 0110 -> 2 -> 1 + dp[n-4]
        # 7: 0111 -> 3 -> 1 + dp[n-4]
        # 8: 1000 -> 1 -> 1 + dp[n-8]
        # 9: 1001 -> 1 -> 1 + dp[n-8]
        # 10: 1010 -> 1 -> 1 + dp[n-8]
        # 11: 1011 -> 1 -> 1 + dp[n-8]
        # 12: 1100 -> 1 -> 1 + dp[n-8]
        # 13: 1101 -> 1 -> 1 + dp[n-8]
        # 14: 1110 -> 1 -> 1 + dp[n-8]
        # 15: 1111 -> 1 -> 1 + dp[n-8]
        # 16: 10000 -> 1 -> 1 + dp[n-16]

        dp = [0] * (n + 1)
        offset = 1 # tracks the power of 2.

        for i in range(1, n + 1):
            print(f"dp |{dp}| === i |{i}| === offset BEFORE|{offset}|")
            if offset * 2 == i:
                offset = i
            print(f"dp |{dp}| === i |{i}| === offset AFTER |{offset}|")
            dp[i] = 1 + dp[i - offset]
        return dp

print(f"15 -> |{Solution().countBits(15)}|")

"""
Runtime: O(nlogn) to run the loop until n.
Space: O(1) to store the count.
"""