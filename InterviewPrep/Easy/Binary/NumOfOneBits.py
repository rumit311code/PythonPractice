"""
https://neetcode.io/problems/number-of-one-bits

Number of One Bits

You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:
Input: n = 00000000000000000000000000010111
Output: 4

Example 2:
Input: n = 01111111111111111111111111111101

Output: 30
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # SOLUTION1: O(1)
        count = 0
        while n:
            count += n % 2 # return 1 if the right most bit is 1 else 0.
            n = n >> 1

        return count

        # # SOLUTION2: O(1) n = n & (n-1)
        # count2 = 0
        # while n:
        #     n = n & (n - 1)
        #     count2 += 1
        #
        # return count2
"""
For both solutions.
Runtime: O(1) because at max it will run for O(32) for 32 bit number for solution1 and COUNT times for solution2.
Space: O(1) to store count.
"""