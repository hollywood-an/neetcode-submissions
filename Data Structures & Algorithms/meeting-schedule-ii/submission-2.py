"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        count = 0
        previous = -1
        for i in intervals:
            if i.start > previous:
                count += 1
            else:
                count = 1
            previous = i.end
        return count