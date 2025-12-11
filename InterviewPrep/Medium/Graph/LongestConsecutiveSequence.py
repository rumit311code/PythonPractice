"""
https://neetcode.io/problems/longest-consecutive-sequence/question

Video: https://www.youtube.com/watch?v=P6RZZMu_maU

Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence
of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly
1 greater than the previous element.
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""

nums1 = [0,3,2,5,4,6,1,1]
nums2 = [2,20,4,10,3,4,5]
nums3 = [9,1,4,7,3,-1,0,5,8,-1,6]
nums4 = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]

class Solution: # use this if all increasing sequences need to be returned
    def longestConsecutive(self, nums: List[int]) -> int:
        print(f"nums before: {nums}")
        nums = sorted(list(set(nums))) # O(n log n)
        print(f"sorted unique nums after: {nums}")

        lcs = []
        lcs_start = 0
        lcs_end = 0
        i = 0
        while i < len(nums)-1: # O(n) loop
            print(f"i: {i}, lcs_start:{lcs_start}, lcs_end:{lcs_end} ===nums=== {nums[i]}")
            if nums[i+1] == nums[i]: # dup element found.
                print(f"dup element found at {i} and {lcs_end}")
                lcs_start =+ 1
            elif nums[i+1] == nums[i] + 1: # next element is 1 higher.
                print(f"found one increment with index {i} and {lcs_start+1}.")
                print(f"{nums[lcs_start+1]}={nums[i]} + 1. increment lcs_end")
                lcs_end += 1 # increase the lcs length.
            else: # end of the lcs.
                lcs.append(nums[lcs_start:lcs_end + 1])
                print(f"OLD lcs_start: {lcs_start}, lcs_end: {lcs_end}")
                lcs_start = i+1
                lcs_end = i+1
                print(f"NEW lcs_start: {lcs_start}, lcs_end: {lcs_end}")
            i += 1

        lcs.append(nums[lcs_start:lcs_end + 1])
        print(f"lcs: {lcs}")
        longest_sequence = len(max(lcs, key=len))
        return longest_sequence

# print(Solution().longestConsecutive(nums1))
# print(Solution().longestConsecutive(nums2))
# print(Solution().longestConsecutive(nums3))
# print(Solution().longestConsecutive(nums4))

"""
Runtime: O(n log n) for sorting + O(n) for while loop = O(n log n) 
Space: O(n) to store lcs
"""

class Solution2: # use this if only count is needed
    def longestConsecutive(self, nums):
        num_set = set(nums) # O(n)
        print(f"nums: {nums}, num_set: {num_set}")
        longest = 0

        # nums2 = [2,20,4,10,3,4,5]
        # lcs1 = [2,3,4,5] -> no preset (n-1 -> 2-1 = 1) for 2 found in the set, so 2 is the start of an LCS.
        # lcs2 = [10] -> no preset (10-1 = 9) for 10 found in the set, so 10 is the start of an LCS.
        # lcs3 = [20] -> no preset (20-1 = 19) for 20 found in the set, so 20 is the start of an LCS.
        # for each LCS, if n+1 is not found in the set, mark that as end of LCS.
        for n in num_set: # O(n)
            print(f"=====checking num {n}")
            # check if "preset" is in the array or not. If not, this is the start of a new LCS.
            if n-1 not in num_set:
                print(f"===== =====new LCS starting at {n}.")
                length = 0
                while (n + length) in num_set: # O(1) look up because of set
                    length += 1
                print(f"===== =====current LCS length: {length}")
                longest = max(longest, length)
                print(f"===== ===== =====longest LCS so far: {longest}")
                # longest LCS is the entire array. no need to iterate further.
                if longest == len(num_set):
                    break
        return longest

print(Solution2().longestConsecutive(nums1))
print(Solution2().longestConsecutive(nums2))
print(Solution2().longestConsecutive(nums3))
print(Solution2().longestConsecutive(nums4))
"""
Runtime: O(n) for making a set + (O(n) for loop * nO(1)) set lookup = O(n)
Space: O(n) to store num_set
"""
