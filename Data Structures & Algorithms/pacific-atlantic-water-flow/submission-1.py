class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        results = []
        visited = set()
        def dfs(i, j, pacific, previous):
            if (i, j) in visited:
                return False
            if (i < 0 or j < 0) and pacific:
                return True

            if (i < 0 or j < 0) and not pacific:
                return False
            
            if (i == len(heights) or j == len(heights[0])) and not pacific:
                return True

            if (i == len(heights) or j == len(heights[0])) and pacific:
                return False

            if heights[i][j] > previous:
                return False 
            visited.add((i,j))
            return dfs(i-1, j, pacific, heights[i][j]) or dfs(i, j-1, pacific, heights[i][j]) or dfs(i+1, j, pacific, heights[i][j]) or dfs(i, j+1, pacific, heights[i][j])
                
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visited.clear()
                pacific = dfs(i, j, True, 1001) 
                visited.clear()
                atlantic = dfs(i, j, False, 1001)
                if pacific and atlantic:
                    results.append([i,j])
            
        return results