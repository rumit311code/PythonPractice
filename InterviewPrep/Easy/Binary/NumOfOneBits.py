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
        while n: # for a 32-bit number, this is max O(32) hence O(1)
            # even numbers have last bit as 0 e.g. 14 -> 1110 -> n % 2 = 0
            # odd numbers have last bit as 1 e.g. 15 -> 1111 -> n % 2 = 1
            # return 1 if the right most bit is 1 (odd numbers) else 0 (even numbers).
            count += n % 2

            # shift one bit right and repeat until we get n=0.
            # Example below for 14 -> 1110
            # loop1: 1110 -> 0111 -> count = 0 # last bit 0 before right shift
            # loop2: 0111 -> 0011 -> count = 1 # last bit 1 before right shift
            # loop3: 0011 -> 0001 -> count = 2 # last bit 1 before right shift
            # loop4: 0001 -> 0000 -> count = 3 # last bit 1 before right shift
            # n = 0000 = False. Loop ends. count = 3
            n = n >> 1
        return count

        # # SOLUTION2: O(1) n = n & (n-1)
        # count2 = 0
        # while n:
        #     n = n & (n - 1)
        #     count2 += 1
        #
        # return count2
        # Example
        # n = 00001100(12)
        # n - 1 = 00001011(11)
        # -----------------
        # AND = 00001000(8)   ← Lowest  1 cleared
"""
For both solutions.
Runtime: O(1) because at max it will run for O(32) for 32 bit number for solution1 and COUNT times for solution2.
Space: O(1) to store count.
"""