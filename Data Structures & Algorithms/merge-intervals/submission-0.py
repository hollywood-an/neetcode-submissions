class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = [intervals[0]]
        for current in intervals[1:]:
            previous = merged[-1]
            if current[0] <= previous[1]:
                merged[-1][1] = current[1]
            else:
                merged.append(current)

        return merged