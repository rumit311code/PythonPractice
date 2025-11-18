"""
https://neetcode.io/problems/products-of-array-discluding-self

Products of Array Except Self

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)?
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20

"""
# calculate prefix multiplication
# calculate postfix multiplication

# FOR PREFIX -> 0 to (len-2) -> O(n) loop -> # not until (len-1) because there won't be a POSTFIX for the LAST element.
# start with currentPrefix = 1 and then put it to 0th index in OUTPUT array
# iterate the INPUT array from 0th index
#   currentPrefix = currentElement * currentPrefix -> also put that to (i+1)th index in the OUTPUT array
# iterate until len-1

# FOR POSTFIX -> (len-1) to 1 -> O(n) loop -> # not until 0 because there won't be a PREFIX for the FIRST element.
# start with currentPrefix = 1 and then put it to (len-1)th index in output array
# iterate the INPUT array from (len-1)th index
# multiply element by currentPrefix -> this is the new currentPrefix and also put that to i-1th index in the output array
# iterate until 1st index

from typing import List

class Solution:
    def product_except_self(self, input: List[int]) -> List[int]:
        output = [1] * len(input)

        # first o(n) loop for PREFIX
        prefix = 1
        for i in range(len(input)):
            output[i] = prefix
            prefix *= input[i]
        print(f"output1 = {output}")

        # second o(n) loop for POSTFIX
        postfix = 1
        for i in range(len(input) - 1, -1 , -1):
            output[i] *= postfix
            postfix *= input[i]
        print(f"output2 = {output}")
        return output

print(f"productExceptSelf of [1,2,4,6] === |{Solution().product_except_self(input=[1,2,4,6])}|")
# print(f"productExceptSelf of [-1,0,1,2,3] === |{Solution().product_except_self(input=[-1,0,1,2,3])}|")
"""
Run time: O(n) - Two times.
Space: None because output array's space is usually not counted. Otherwise its O(n).
"""