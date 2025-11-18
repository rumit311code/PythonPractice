"""
https://neetcode.io/problems/longest-increasing-subsequence

Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by
deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".

Example 1:
Input: nums = [9,1,4,2,3,3,7]
Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:
Input: nums = [0,3,1,3,2,3]
Output: 4 because of [0,1,2,3]

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""
from typing import List


# recursive: foreach num, get subseq with num and without num,
# only include num if prev was less, cache solution of each;
# dp=subseq length which must end with each num, curr num must be after a prev dp or by itself;
#
# Solution1: brute force with depth first search -> 2^n -> BAD approach
#   for each element recursively up to the final element, check if it will be in the subsequence or not.
#
# Solution2: improve brute force with caching -> Reduces to O(n^2)
#
#   Start with last index and go up to the first index.
#
# sample array: [1,2,4,3] -> length(n) = 4, highest index = n-1 = 3
# LIS[n-1] = 1 -> because there is no other element left after element at the last index.
# keep going backwards from n-1th to 0th index.
# LIS[i]= max(1, 1+LIS[i+1],..., 1+LIS[n]) -> Take those LIS where num[i] < num[i+1...n]
#
# LIS[3] = 1
# LIS[2] = max(1, 1+LIS[2+1]), BUT num[2] > num[2+1], so DON'T take LIS[3]
#   so, LIS[2] = max(1) = 1
# LIS[1] = max(1, 1 + LIS[1+1], 1 + LIS[1+2]) = max(1, 1+1, 1+1) = 2
#   because num[1] < num[1+1] and num[1] < num[1+2]
# LIS[0]= max(1, 1 + LIS[0+1], 1 + LIS[0+2], 1 + LIS[0+3]) = max(1, 1+2, 1+1, 1+1) = 3
#    because num[0] < num[1+1], num[0] < num[1+2] and num[0] < num[1+2]
# Max between LIS[0], LIS[1], LIS[2] and LIS[3] is 3.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1): # O(n) loop
            for j in range(i + 1, len(nums)): # O(n) loop
                if nums[i] < nums[j]: # element at a higher index must be more than the lower index
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)

print(f"[9,1,4,2,3,3] |{Solution().lengthOfLIS([9,1,4,2,3,3])}|")
"""
Runtime: O(n^2)
Space: O(n) to store LIS of length nums.
"""