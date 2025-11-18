"""
https://neetcode.io/problems/sum-of-two-integers

Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:
Input: a = 1, b = 1
Output: 2

Example 2:
Input: a = 4, b = 7
Output: 11

Constraints:
-1000 <= a, b <= 1000
"""

# use binary representation and then use XOR and && operators.
# do XOR a ^ b
    # 1 | 0 -> 1
    # 0 | 1 -> 1
    # 0 | 0 -> 0
    # 1 | 1 -> 0 with 1 carry
# do logical AND: && is 1 then we have a carry and we need to shift left
    # 1 | 1 -> 1
    # all others -> 0
# repeat

class Solution:
    def sum(self, a: int, b: int) -> int:
        # Solution 1: which does not work for large / negative numbers.
        # while b != 0:
        #     carry = a & b # &
        #     a = a ^ b # XOR
        #     b = carry << 1 # shift left
        # return a # final sum

        # Solution 2: works for numbers from -1000 to 1000.

        # 32-bit mask in hexadecimal
        mask = 0xFFFFFFFF
        # Max integer for 32-bit signed int
        max_int = 0x7FFFFFFF

        while b != 0:
            # carry contains common set bits of a and b
            carry = (a & b) & mask
            # sum of bits where at least one of the bits is not set
            a = (a ^ b) & mask
            # carry shifted left
            b = (carry << 1) & mask

        # if a is negative, convert to Python's negative integer representation
        if a > max_int:
            a = ~(a ^ mask)

        return a

print(Solution().sum(1, 1))
print(Solution().sum(-1, 1))
print(Solution().sum(-1, -1))
print(Solution().sum(1, -1))
print(Solution().sum(-1000, 1000))
print(Solution().sum(1000, 1000))
print(Solution().sum(-1000, -1000))
print(Solution().sum(1000, -1000))
print(Solution().sum(-10000, 10000))
print(Solution().sum(10000, 10000))
print(Solution().sum(-10000, -10000))
print(Solution().sum(10000, -10000))
"""
Runtime: O(1) for numbers less than 1000. for large numbers it could go up to O(n).
Space: O(1) to store a, b and carry
"""