class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, val in enumerate(heights):
            start = i
            while stack and val < stack[-1][1]:
                height_i, height = stack.pop()
                area = max(area, height * (i-height_i))
                start = height_i
            stack.append((start, val))
            area = max(area, val)
        
        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        return area