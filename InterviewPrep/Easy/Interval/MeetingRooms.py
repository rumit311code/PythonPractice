"""
https://neetcode.io/problems/meeting-schedule/question

Video: https://www.youtube.com/watch?v=PaJxqZVPhbg

Meeting Rooms

Given an array of meeting time interval objects consisting of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict

Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start) # O(nlogn)

        previous = intervals[0]
        print(f"previous: start -> {previous.start}, end -> {previous.end}")
        for current in intervals[1:]: # O(n) loop
            print(f"====current: start -> {current.start}, end -> {current.end}")
            if current.start < previous.end: # overlap
                print("==== ====Found overlap.")
                return False
            else:
                # update previous.
                previous = current
            print(f"=====previous: start -> {previous.start}, end -> {previous.end}")
        return True

        # Without using previous
        for i in range(1, len(intervals)):  # O(n) loop
            previous = intervals[i-1]
            current = intervals[i]
            if current.start < previous.end:  # overlap
                return False
        return True

interval1 = Interval(0, 30)
interval2 = Interval(5, 10)
interval3 = Interval(15, 20)
intervals1 = [interval1, interval2, interval3]

interval4 = Interval(5, 8)
interval5 = Interval(9, 15)
intervals2 = [interval4, interval5]

print(Solution().canAttendMeetings(intervals1)) # False
print(Solution().canAttendMeetings(intervals2)) # True

"""
Runtime: O(n) + O(nlong) = O(nlogn)
Space: O(1) to store previous interval.
"""
