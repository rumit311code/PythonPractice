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
class Solution:
    def sum(self, a: int, b: int) -> int:
        ######
        ###### Solution 1: which does not work for large / negative numbers.
        ######
        # while b != 0:
        #     carry = a & b # &
        #     a = a ^ b # XOR
        #     b = carry << 1 # shift left
        # return a # final sum
        #

        ######
        ###### Solution 2: works for numbers from -Max int to +Max int.
        ######
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
        ###### Solution1: Example for  9 + 11 = 20
        # a = 9 -> 1001
        # b = 11-> 1011
        # c = 20 -> 10100
        #
        # loop1: add 1001 (a) and 1011 (b)
        #   a ^ b -> 1001 ^ 1011 -> XOR
        #       1 ^ 1 -> 0 (will have a carry)
        #       0 ^ 0 -> 0
        #       0 ^ 1 -> 1
        #       1 ^ 1 -> 0  (will have a carry)
        #       0010
        #   a & b (to get carry) -> 1001 & 1011
        #       1 & 1 -> 1
        #       0 & 0 -> 0
        #       0 & 1 -> 0
        #       1 & 1 -> 1
        #       1001 -> shift left -> 10010 (new b)
        #
        # loop2: add 0010 (new a) and 10010 (new b)
        #   a ^ b -> 00010 ^ 10010 -> XOR
        #       0 ^ 1 -> 1
        #       0 ^ 0 -> 0
        #       0 ^ 0 -> 0
        #       1 ^ 1 -> 0
        #       0 ^ 0 -> 0
        #       10000 (new a)
        #   a & b (to get carry) -> 00010 & 10010
        #       0 & 1 -> 0
        #       0 & 0 -> 0
        #       0 & 0 -> 0
        #       1 & 1 -> 1
        #       0 & 0 -> 0
        #       00010 -> shift left -> 00100 (new b)
        #
        # loop3: add 10000 (new a) and 00100 (new b)
        #   a ^ b -> 10000 ^ 00100 -> XOR
        #       1 ^ 0 -> 1
        #       0 ^ 0 -> 0
        #       0 ^ 1 -> 1
        #       0 ^ 0 -> 0
        #       0 ^ 0 -> 0
        #       10100 (new a) -> ANSWER
        #   a & b (to get carry) -> 10000 & 00100
        #       1 & 0 -> 0
        #       0 & 0 -> 0
        #       0 & 1 -> 0
        #       0 & 0 -> 0
        #       0 & 0 -> 0
        #       00000 -> shift left -> 00000 (new b) = 0 -> loop ends.

        ###### Solution2: Example1: positive number with mask
        #  a = 5 = 00000000 00000000 00000000 00000101 # 32 bit representation
        #  b = 7 = 00000000 00000000 00000000 00000111 # 32 bit representation
        #
        # Iteration 1
        #     carry = (a & b) & mask
        #         a & b = 00000000 00000000 00000000 00000101
        #         AND 00000000 00000000 00000000 00000111
        #         = 00000000 00000000 00000000 00000101 (decimal 5)
        #
        #         & mask does nothing visible here (they’re already 32‑bit), but logically says “keep only 32 bits”.
        #
        #     a = (a ^ b) & mask
        #         a ^ b = 00000000 00000000 00000000 00000101
        #         XOR 00000000 00000000 00000000 00000111
        #         = 00000000 00000000 00000000 00000010 (decimal 2)
        #
        #         & mask again just ensures 32‑bit.
        #
        #     b = (carry << 1) & mask
        #         carry << 1 = 00000000 00000000 00000000 00001010 (decimal 10)
        #
        #         & mask trims to 32 bits (no visible change).
        # Now: a = 2, b = 10
        #
        # Iteration 2
        #     carry = (a & b) & mask
        #         a & b = 00000000 00000000 00000000 00000010
        #         AND 00000000 00000000 00000000 00001010
        #         = 00000000 00000000 00000000 00000010 (2)
        #
        #     a = (a ^ b) & mask
        #         a ^ b = 00000000 00000000 00000000 00000010
        #         XOR 00000000 00000000 00000000 00001010
        #         = 00000000 00000000 00000000 00001000 (8)
        #
        #     b = (carry << 1) & mask
        #         carry << 1 = 00000000 00000000 00000000 00000100 (4)
        #
        # Now: a = 8 b = 4
        #
        # Iteration 3
        #     carry = (a & b) & mask
        #         a & b = 00000000 00000000 00000000 00001000
        #         AND 00000000 00000000 00000000 00000100
        #         = 00000000 00000000 00000000 00000000 (0)
        #
        #     a = (a ^ b) & mask
        #         a ^ b = 00000000 00000000 00000000 00001100 (12)
        #
        #     b = (carry << 1) & mask
        #         carry = 0, so b = 0.
        #
        # Loop stops (b == 0), result candidate is a = 12.
        # Now a <= max_int so we just return 12. No sign conversion needed.
        #
        ###### Solution2: Example2: negative number with mask
        #
        # Use 32‑bit two’s complement:
        #     +5 = 00000000 00000000 00000000 00000101
        #
        #     -5 is ~5 + 1 in 32 bits:
        #         ~5 = 11111111 11111111 11111111 11111010
        #         +1 = 00000000 00000000 00000000 00000001
        #         so -5 = 11111111 11111111 11111111 11111011
        #
        # So initial:
        #     a = -5 represented as 11111111 11111111 11111111 11111011 (in 32 bits)
        #     b = 7 00000000 00000000 00000000 00000111
        #
        # Internally Python may store more bits for -5, but "&" mask will keep only the LOWEST 32.
        #
        # Iteration 1
        #
        #     Apply mask to both conceptual values:
        #         a & mask = 11111111 11111111 11111111 11111011
        #         b & mask = 00000000 00000000 00000000 00000111
        #
        #     carry = (a & b) & mask
        #         a & b = 00000000 00000000 00000000 00000011 (3)
        #         & mask keeps 32 bits (still 3).
        #
        #     a = (a ^ b) & mask
        #         a ^ b = 11111111 11111111 11111111 11111011
        #         XOR 00000000 00000000 00000000 00000111
        #         = 11111111 11111111 11111111 11111100
        #
        #     b = (carry << 1) & mask
        #         carry << 1 = 00000000 00000000 00000000 00000110 (6)
        #
        # Now:
        #     a = 11111111 11111111 11111111 11111100
        #     b = 00000000 00000000 00000000 00000110
        #
        # Iteration 2
        #
        #     carry = (a & b) & mask
        #         a & b = 00000000 00000000 00000000 00000100 (4)
        #
        #     a = (a ^ b) & mask
        #         a ^ b = 11111111 11111111 11111111 11111100
        #         XOR 00000000 00000000 00000000 00000110
        #         = 11111111 11111111 11111111 11111010
        #
        #     b = (carry << 1) & mask
        #         carry << 1 = 00000000 00000000 00000000 00001000 (8)
        #
        # Now:
        #     a = 11111111 11111111 11111111 11111010
        #     b = 00000000 00000000 00000000 00001000
        #
        # Iteration 3
        #
        #     carry = (a & b) & mask
        #         a & b = 00000000 00000000 00000000 00001000 (8)
        #
        #     a = (a ^ b) & mask
        #         a ^ b = 11111111 11111111 11111111 11111010
        #         XOR 00000000 00000000 00000000 00001000
        #         = 11111111 11111111 11111111 11110010
        #
        #     b = (carry << 1) & mask
        #         carry << 1 = 00000000 00000000 00000000 00010000 (16)
        #
        # Now:
        #     a = 11111111 11111111 11111111 11110010
        #     b = 00000000 00000000 00000000 00010000
        #
        # Keep iterating; if you carry this through to completion, eventually b becomes 0 and:
        #   final 32‑bit a = 00000000 00000000 00000000 00000010 (which is +2 in two’s complement).
        #
        # In this case, the mathematical sum is +2 (a small positive), so the sign bit (31st) is 0 and a <= max_int;
        #   the return path just returns a. The mask has ensured that, even though "Python might try to
        #   add infinite leading 1s for negatives", only the BOTTOM 32 bits participate in the algorithm.
        #
        # Why the final return a if a <= max_int else ~(a ^ mask)
        #   - After the loop, "a" holds a 32‑bit pattern, but Python still treats it as a non‑fixed‑width integer.
        #   - If the 31st bit (sign bit) is 0, the two’s complement 32‑bit interpretation is non‑negative
        #       and matches the usual Python integer value, so a is fine.
        #   - If the 31st bit is 1, then in 32‑bit two’s complement that pattern represents a negative number.
        #       To make Python’s unbounded integer take the same value, the code computes:
        #
        #       a ^ mask: FLIPS the LOWER 32 bits (creates the INVERTED pattern within 32 bits).
        #       ~(a ^ mask): FLIPS ALL bits; effectively it:
        #           - KEEPS the LOWER 32 bits the same as original "a"
        #           - sets all HIGHER bits to 1, giving the correct infinite leading‑1 form of a negative integer.