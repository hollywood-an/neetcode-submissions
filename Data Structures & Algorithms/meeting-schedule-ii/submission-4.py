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
        count = [[intervals[0]]]
        previous = intervals[0].end
        for i in intervals[1:]:
            if i.start >= previous:
                count[len(count)-1].append(i)
            else:
                count.append([i])
            previous = i.end
        return len(count)

