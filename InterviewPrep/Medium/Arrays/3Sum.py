"""
https://neetcode.io/problems/three-integer-sum

3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5

"""
from typing import List

# sort input
# for each first element, find next two where -a = b+c,
# if a=prevA, skip a
# if b=prevB skip b to elim duplicates;
# to find b,c use two pointers, left/right on remaining list;

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort() # O(nlogn)
        print(f"nums |{nums}|")

        for index, val in enumerate(nums): # outer O(n) loop for a.
            print(f"index|val|nums[index]|nums[index - 1]| ---- |{index}|{val}|{nums [index]}|{nums [index - 1]}|")
            if index > 0 and val == nums[index - 1]:
                print("dup element found")
                continue # if dup move to the next element

            l, r = index + 1, len(nums) - 1 # start with 2nd and last element for b(left pointer) and c(right pointer).
            while l < r: # inner O(n) loop for b and c, and hence O(n^2)
                print(f"val|l|nums[l]|r|nums[r]| ---- |{val}|{l} -> {nums[l]}|{r} -> {nums[r]}|")

                threeSum = val + nums[l] + nums[r] # this can be any target. the program below is for 0.
                print(f"threeSum| ---- |{threeSum}|")

                if threeSum > 0: # sum more than target, reduce c.
                    r -= 1 # decrease right pointer
                elif threeSum < 0: # sum less than target, increase b.
                    l += 1 # increase left pointer
                else: # found a triplet.
                    print(f"TRIPLET found: val | nums[l] | nums[r] | ---- |{val}|{nums[l]}|{nums[r]}|")
                    res.append([val, nums[l], nums[r]]) # found a triplet
                    l += 1 # increase b and keep iterating up to c.
                    while nums[l] == nums[l - 1] and l < r: # if dup b element is found, move to the next b.
                        l += 1
        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))
"""
Run time: sorting O(nlogn) + loop of O(n^2) -> O(n^2)
Space: average O(1), worst: O(n) -> to store the triplets.
"""