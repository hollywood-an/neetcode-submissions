class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        second = len(heights) - 1
        max  = 0
        while first < second:
            if max < min(heights[first], heights[second]) * (second-first):
                max = min(heights[first], heights[second]) * (second-first)
            if heights[first] < heights[second]:
                first = first + 1
            else:
                second = second - 1
        return max