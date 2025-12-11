"""
https://neetcode.io/problems/merge-intervals/question

Video: https://www.youtube.com/watch?v=44H3cEC2fFM

Merge Intervals

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point.
For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:
Input: intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]

Example 2:
Input: intervals = [[1,2],[2,3]]
Output: [[1,3]]

Example 3:
Input: intervals = [[1,3],[8,10],[15,18],[2,6]]
Output: [[1,6],[8,10],[15,18]]

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by start
        print(f"intervals BEFORE: {intervals}")
        intervals.sort(key=lambda i: i[0]) # O(nlogn)
        print(f"intervals AFTER: {intervals}")

        res = [intervals[0]]
        print(f"res BEFORE: {res}")
        for start, end in intervals[1:]:
            print(f"=====: res -> {res}, start -> {start}, end -> {end}")
            print(f"=====: res[-1] -> {res[-1]}")
            print(f"=====: res[-1][1] -> {res[-1][1]}")
            # end of most recent interval
            # index -1 = 1st element from the length of the array. basically last.
            last_end = res[-1][1]

            # overlapping intervals.
            if start <= last_end:
                print(f"===== ===== overlap found. update end for previous.")
                # [1,5] and [2,4] -> [1,5]
                # [1,5] and [2,6] -> [1,6]
                # in both cases 2 (start of current) < 5 (end of last)
                res[-1][1] = max(last_end, end)
            else: # no overlap
                # [1,5] and [7,8] -> just add [7,8] as is.
                res.append([start,end])
            print(f"===== =====: Updated res -> {res}")

        return res

print(Solution().merge(intervals=[[2,8],[1,4],[3,9]]))
print(Solution().merge(intervals=[[1,3],[1,5],[6,7]]))
print(Solution().merge(intervals=[[1,5],[6,7]]))
print(Solution().merge(intervals=[[1,3],[8,10],[15,18],[2,6]]))

"""
Runtime: # O(nlogn) for sorting + O(n) to iterate over intervals = # O(nlogn)
Space: O(n) to store res.
"""
