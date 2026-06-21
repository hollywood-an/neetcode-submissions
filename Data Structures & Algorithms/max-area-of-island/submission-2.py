class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        visit = set()
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            if i+j in visit:
                return 0
            visit.add(i+j)
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, dfs(i, j))

        return area