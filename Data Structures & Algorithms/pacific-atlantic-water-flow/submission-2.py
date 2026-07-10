class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        results = []
        pacific, atlantic = set(), set()
        def dfs(i, j, visited, previous):
            if i<0 or j<0 or i == len(heights) or j == len(heights[0]) or (i, j) in visited or previous > heights[i][j]:
                return
            visited.add((i, j))
            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
        
        for i in range(len(heights)):
            dfs(i, 0, pacific, -1)
            dfs(i, len(heights[0]) - 1, atlantic, -1)
        
        for j in range(len(heights[0])):
            dfs(0, j, pacific, -1)
            dfs(len(heights)-1, j, atlantic, -1)
                
        for pos in pacific:
            if pos in atlantic:
                results.append(pos)
            
        return results