"""
https://neetcode.io/problems/meeting-schedule-ii/question

Video: https://www.youtube.com/watch?v=FdzJmTCVyJU

Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number
of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:
Input: intervals = [(4,9)]
Output: 1

Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        elif len(intervals) == 1:
            return 1

        start = sorted([interval.start for interval in intervals]) # O(n) + O(n logn)
        end = sorted([interval.end for interval in intervals]) # O(n) + O(n logn)

        print(f"start: {start}")
        print(f"end: {end}")

        res, days = 0, 0
        start_counter, end_counter = 0, 0

        while start_counter < len(intervals): # O(n)
            if start[start_counter] < end[end_counter]:
                # meeting is still going on, need another day
                start_counter += 1
                days += 1
            else:
                # meeting ended. new meeting can be done on the same day.
                end_counter += 1
                days -= 1
            res = max(res, days) # to keep the max number of days needed so far.
        return res

interval1 = Interval(0, 40)
interval2 = Interval(5, 10)
interval3 = Interval(15, 20)
intervals1 = [interval1, interval2, interval3]

interval4 = Interval(5, 8)
interval5 = Interval(9, 15)
intervals2 = [interval4, interval5]

interval6 = Interval(1, 5)
interval7 = Interval(2, 6)
interval8 = Interval(3, 7)
interval9 = Interval(4, 8)
interval10 = Interval(5, 9)
intervals3 = [interval6, interval7, interval8, interval9, interval10]

print(Solution().minMeetingRooms(intervals1))  # 2 days
print(Solution().minMeetingRooms(intervals2))  # 1 day
print(Solution().minMeetingRooms(intervals3))  # 4 days

"""
Runtime: O(n) + O(nlogn) for sorting + O(n) to iterate over intervals = O(nlogn)
Space: O(n) for start + O(n) for end + O(1) for counters = O(n)
"""