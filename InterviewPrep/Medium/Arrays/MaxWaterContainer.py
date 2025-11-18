"""
https://neetcode.io/problems/max-water-container

Container With Most Water

You are given an integer array heights where heights[i] represents the height of the
i th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
"""
import time
from typing import List

# APPROACH1: Brute force -> O(n^2)
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        start_time = time.time()
        max_area = 0

        for l in range(len(height)):
            for r in range(l +1, len(height)):
                max_area = max(max_area, (r - l) * min(height[l], height[r]))
        print(f"Time taken ===|{time.time() - start_time}|")
        return max_area

# APPROACH2: Two pointers, binary search -> O(n)
# start with left most and right most pointers -> calculate area.
# if L < R -> shift right, otherwise shift left -> calculate area and update to max and repeat.
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        start_time = time.time()
        max_area = 0

        l = 0
        r = len(height) - 1
        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]: # shift right
                l += 1
            else: # shift left
                r -= 1
        print(f"Time taken ===|{time.time() - start_time}|")
        return max_area

print(f"[1,7,2,5,4,7,3,6] === |{Solution1().maxArea(height = [1,7,2,5,4,7,3,6])}|")
print(f"[2,2,2] === |{Solution1().maxArea(height = [2,2,2])}|")

print(f"[1,7,2,5,4,7,3,6] === |{Solution2().maxArea(height = [1,7,2,5,4,7,3,6])}|")
print(f"[2,2,2] === |{Solution2().maxArea(height = [2,2,2])}|")
"""
Runtime: O(n) because looping at max once.
Space: O(1) to store the area.
"""