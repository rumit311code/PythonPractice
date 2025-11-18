"""
https://neetcode.io/problems/reverse-bits

Reverse Bits

Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:
Input: n = 00000000000000000000000000010101
Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21,
gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.
"""
# Solution1: bit32 format of string to add leading 0s -> slice to reverse -> recast to int with base 2.
class Solution1:
    def to_32bit_unsigned(self, n) -> str:
        return format(n, '032b')

    def to_32bit_signed(self, n) -> str:
        return format(n & 0xFFFFFFFF, '032b')

    def reverseBits(self, n: int) -> int:
        # This will not work because it's not 32 bits
        print(f"n: {n}")
        print(f"bin(n): {bin(n)}") # 21: 0b10101, -21: -0b10101
        # print(f"str(bin(n))[2:]: {str(bin(n))[2:]}") # for negative, [3:]
        # print(f"str(bin(n))[2:][::-1]: {str(bin(n))[2:][::-1]}")
        # print(f"int(str(bin(n))[2:][::-1]): {int(str(bin(n))[2:][::-1], 2)}")

        # works only for unsinged (positive) int
        # print(f"to_32bit_unsigned: {self.to_32bit_unsigned(n)}") # 21: 00000000000000000000000000010101
        # print(f"to_32bit_unsigned[::-1]: {self.to_32bit_unsigned(n)[::-1]}") # 10101000000000000000000000000000
        # print(f"to_32bit_unsigned[::-1]: {int(self.to_32bit_unsigned(n)[::-1], 2)}") # 2818572288

        # works for both signed and unsinged int
        print(f"to_32bit_signed: {self.to_32bit_signed(n)}") # 21: 00000000000000000000000000010101
        print(f"to_32bit_signed[::-1]: {self.to_32bit_signed(n)[::-1]}") # 10101000000000000000000000000000
        print(f"to_32bit_signed[::-1]: {int(self.to_32bit_signed(n)[::-1], 2)}") # 2818572288
        return int(self.to_32bit_signed(n)[::-1], 2)

# print(Solution1().reverseBits(21))
# print(Solution1().reverseBits(-21))
"""
Runtime: O(1) because its always 32 bit

String to number (int())- O(n) n = length of string (digits) -> but in this case it is O(1) -> because its 32 bits always
Number to string (str())- O(log N) N = numeric value -> at max this is 32. So this is O(1) too.
String reverse (s[::-1])- O(n) n = length of string -> this is always (32) -> so O(1)

Space: O(1)
"""
# Solution2: bitwise shift to reverse the binary representation.
class Solution2:
    def to_32bit_signed(self, n) -> str:
        return format(n & 0xFFFFFFFF, '032b')

    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            print(f"i |{i}|")
            print(f"n |{self.to_32bit_signed(n)}|")
            print(f"res |{self.to_32bit_signed(res)}|")
            print(f"(n >> i) |{self.to_32bit_signed((n >> i))}|")
            print(f"(n >> i) & 1 |{self.to_32bit_signed((n >> i) & 1)}|")
            bit = (n >> i) & 1
            print(f"bit << (31 -i) |{self.to_32bit_signed(bit << (31 -i))}|")
            print(f"res | bit << (31 -i) |{self.to_32bit_signed(res | (bit << (31 -i)))}|")
            res = res | (bit << (31 -i))
            print("===================================")
        return res

"""
Runtime: O(1) because its always 32 loops irrespective of the number.
Space: O(1)
"""

print(Solution2().reverseBits(21))
print(Solution2().reverseBits(-21))
