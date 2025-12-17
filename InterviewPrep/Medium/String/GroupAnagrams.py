"""
https://neetcode.io/problems/anagram-groups/question

Video: https://www.youtube.com/watch?v=vzdNOK2oB2E

Group Anagrams

Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as
another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs: #O(n)
            sorted_d = dict(sorted(Counter(s).items())) #O(len(s))
            key = ''.join(k + str(v) for k, v in sorted_d.items()) #O(num of diff chars)
            res.setdefault(key, []).append(s)
        return list(res.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))

"""
Runtime: O(n . len(s))
Space: O(n) to store sorted dict + O(n) for res = O(n)
"""