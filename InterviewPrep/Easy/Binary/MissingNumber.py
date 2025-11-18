"""
https://neetcode.io/problems/missing-number

Missing Number

Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in
the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:
Input: nums = [1,2,3]
Output: 0
Explanation: Since there are 3 numbers, the range is [0,3]. The missing number is 0 since it does not appear in nums.

Example 2:
Input: nums = [0,2]
Output: 1

Constraints:

1 <= nums.length <= 1000
"""
from typing import List


# SOLUTION 1: Using XOR (Runtime: O(n) and Space: O(1))
# use XOR because (n ^ n = 0) and (0 ^ n = n)
# also order does not matter for XOR with multiple numbers
# so (0 ^ 3 ^ 5 = 3 ^ 5 ^ 0)
# Example for input array [0,2]
#   A. input array: [0, 2]
#   B. final array: input array has 2 elements, so the final array from 0 to range(2 elements): [0, 1, 2]
#   C. missing number: 1
#   when we do A(input array) ^ B(final array) -> we get C (missing number ~ 1)

# SOLUTION 2: Using sums (Runtime: O(n) and Space: O(1))
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([i for i in range(len(nums)+1)]) - sum(nums)

print(f"1[0,2]: {Solution2().missingNumber([0,2])}")
print(f"1[0,1,2]: {Solution2().missingNumber([0,1,2])}")
print(f"1[0,1,2,3]: {Solution2().missingNumber([0,1,2,3])}")
print(f"1[1,2,3]: {Solution2().missingNumber([1,2,3])}")

# SOLUTION 3: Using diff while creating the final array (Runtime: O(n) and Space: O(1))
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # final number in the final_array

        for i in range(len(nums)):
            res += (i - nums[i]) # add index , subtract input array element value.
        return res # the final result will be the missing number.

print(f"2[0,2]: {Solution3().missingNumber([0,2])}")
print(f"2[0,1,2]: {Solution3().missingNumber([0,1,2])}")
print(f"2[0,1,2,3]: {Solution3().missingNumber([0,1,2,3])}")
print(f"2[1,2,3]: {Solution3().missingNumber([1,2,3])}")

"""
Runtime: O(2n) because iterating one/two arrays in sequence -> so O(n)
Space: O(1): to store the result
"""