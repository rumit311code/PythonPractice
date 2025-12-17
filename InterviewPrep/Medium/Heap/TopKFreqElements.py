"""
https://neetcode.io/problems/top-k-elements-in-list/question

Video: https://www.youtube.com/watch?v=YPTqKIgVk-k

Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

from collections import Counter

class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        # key=lambda item: item[1] -> sorts dictionary by values
        # reverse=True -> for descending order (large to small).
        # sorted(d.items()) -> sorts  dictionary by keys
        # sorted returns list of tuples.
        # dict(sorted(...)) -> converts the list of tuples to dict.
        sorted_by_value_desc = dict(sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True))
        return list(sorted_by_value_desc.keys())[:k]
        """
        Runtime: O(n) for creating counter + O(nlogn) for sort + O(n) for dict + O(n) for slice -> O(nlogn)
        Space: O(n) to store counter
        """

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        """
        Runtime: O(klogn)
        Space: O(n) to store count and freq.
        """
print(Solution().topKFrequent1([1,2,2,3,3,3], 2))
print(Solution().topKFrequent1([7,7], 1))
print(Solution().topKFrequent1([1,2], 2))