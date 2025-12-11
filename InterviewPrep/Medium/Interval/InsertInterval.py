"""
https://neetcode.io/problems/insert-new-interval/question

Video: https://www.youtube.com/watch?v=A8NUOmlwOlM

Insert Interval

You are given an array of non-overlapping intervals where
intervals[i] = [start_i, end_i] represents the start and the end time of the
ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order
by start_i and also intervals still does not have any overlapping intervals.
You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point.
For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

Example 1:
Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
Output: [[1,6]]

Example 2:
Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
Output: [[1,2],[3,5],[6,7],[9,10]]

Constraints:

0 <= intervals.length <= 1000
newInterval.length == intervals[i].length == 2
0 <= start <= end <= 1000
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Example 1: with overlap.
        # 1..3.....4..6  [1,3] , [4,6]
        #   2........5   [2,5]
        # 1...........6  [1,6]

        # Example 2: no overlap.
        # 1..2.....3..5..... .....9..10     [1,2],[3,5],[9,10]
        #                  6..7             [6,7]
        # 1..2.....3..5.....6..7.....9..10  [1,2],[3,5],[6,7],[9,10]

        res = []
        for i in range(len(intervals)):
            # no overlapping.
            # newInterval is less than the current interval.
            if newInterval[1] < intervals[i][0]:
                # insert the new interval first.
                res.append(newInterval)
                # all other current intervals are higher than the newInterval.
                # so, just add them to the result and return.
                return res + intervals[i:]

            # no overlapping.
            # newInterval START is more than END of the current interval.
            # add the current interval as is to the result.
            # and continue to check other intervals with the newInterval.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # newInterval is overlapping.
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        res.append(newInterval)
        return res

print(Solution().insert(intervals=[[1,3],[4,6]], newInterval=[2,5]))
print(Solution().insert(intervals=[[1,2],[3,5],[9,10]], newInterval=[6,7]))

"""
Runtime: O(n) to iterate over intervals once.
Space: O(n) to store res.
"""