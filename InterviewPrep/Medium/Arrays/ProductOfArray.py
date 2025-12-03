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

# FOR PREFIX -> product of all numbers BEFORE n
# 0 to (len-2) -> O(n) loop -> # not until (len-1) because there won't be a POSTFIX for the LAST element.
# start with currentPrefix = 1 and then put it to 0th index in OUTPUT array
# iterate the INPUT array from 0th index
#   currentPrefix = currentElement * currentPrefix -> also put that to (i+1)th index in the OUTPUT array
# iterate until len-1

# FOR POSTFIX -> product of all numbers AFTER n
# (len-1) to 1 -> O(n) loop -> # not until 0 because there won't be a PREFIX for the FIRST element.
# start with currentPrefix = 1 and then put it to (len-1)th index in output array
# iterate the INPUT array from (len-1)th index
# multiply element by currentPrefix -> this is the new currentPrefix and also put that to i-1th index in the output array
# iterate until 1st index

from typing import List

class Solution:
    def product_except_self(self, input: List[int]) -> List[int]:
        # [1,2,3,4]
        # n=4
        #
        # prefix[-1] = 1 -> there is no prefix for input[0] so, default to 1.
        # prefix = [
        #           (input[0] = 1) * (prefix = 1) = 1,
        #           (input[1] = 2) * (prefix = 1) = 2,
        #           (input[2] = 3) * (prefix = 2) = 6,
        #           (input[3] = 4) * (prefix = 6) = 24,
        #           ]
        # prefix -> [1,2,6,24]
        #
        # postfix[4] = 1 -> -> there is no prefix for input[3] so, default to 1.
        # [24, 24, 12, 4] -> index from n-1 to 0 -> postfix[n] = 1
        # postfix = [
        #           (input[3] = 4) * (postfix = 1) = 4,
        #           (input[2] = 3) * (postfix = 4) = 12,
        #           (input[1] = 2) * (postfix = 12) = 24,
        #           (input[0] = 1) * (postfix = 24) = 24,
        #           ]
        # postfix = [24,24,12,4]
        #
        # For the output array -> prefix = n-1, postfix = n+1
        # output = [
        #           output[0]=prefix[-1] * postfix[1] -> 1*24=24,
        #           output[1]=prefix[0] * postfix[2] -> 1*12=12,
        #           output[2]=prefix[1] * postfix[3] -> 2*4=8,
        #           output[3]=prefix[2] * postfix[4] -> 6*1=6,
        #           ]
        # output = [24,12,8,6]
        # The above solution uses prefix and postfix arrays so Space is O(n) + O(n) = O(n).
        #   This can be optimized by storing and updating output array directly with the prefix and postfix values.
        #   This will result in O(1) since no other storage is needed.

        output = [1] * len(input) # start with output=[1,1,1,1]

        # first o(n) loop for PREFIX
        prefix = 1 # start with prefix[-1]=1 -> there is no prefix for input[0]
        for i in range(len(input)):
            output[i] = prefix # NOT creating prefix array and storing its values in output array.
            prefix = prefix * input[i]
        print(f"output1 = {output}")
        # output = [1,1,2,6]

        # second o(n) loop for POSTFIX
        postfix = 1 # start with postfix[4]=1 -> there is no postfix for input[3]
        for i in range(len(input) - 1, -1 , -1): # i=3,2,1,0
            # output[i] = prefix[i]
            output[i] = output[i] * postfix # # NOT creating postfix array and storing its values in output array.
            # 6 = 6 * 1
            # 8 = 2 * 4
            # 12 = 1 * 12
            # 24 = 1 * 24
            postfix = postfix * input[i] # keep updating postfix for next iteration without storing in an array.
            # 4 = 1 * 4
            # 12 =4 * 3
            # 24 = 12 * 2
            # 24 = 24 * 1
        print(f"output2 = {output}")
        # output = [24,12,8,6]
        return output

print(f"productExceptSelf of [1,2,3,4] === |{Solution().product_except_self(input=[1,2,4,6])}|")
# print(f"productExceptSelf of [-1,0,1,2,3] === |{Solution().product_except_self(input=[-1,0,1,2,3])}|")
"""
Run time: O(n) + O(n) -> O(n)
Space: None because output array's space is usually not counted. Otherwise its O(n).
"""