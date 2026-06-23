class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(i, j):
            queue = deque([[(i, j)]])
            visited = set([(i, j)])
            count = 0
            found = False
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while queue:
                level = queue.popleft()
                nextlevel = []
                for n in level:
                    row, col = n
                    if grid[row][col] == 0:
                        found = True
                        break
                    if grid[row][col] == -1:
                        continue
                    if row + 1 < len(grid):
                        if (row + 1, col) not in visited:
                            visited.add((row+1, col))
                            nextlevel.append((row + 1, col)) 
                    if row - 1 > -1:
                        if (row - 1, col) not in visited:
                            visited.add((row-1, col))
                            nextlevel.append((row - 1, col))  
                    if col + 1 < len(grid[0]):
                        if (row, col+1) not in visited:
                            visited.add((row, col+1))
                            nextlevel.append((row, col+1)) 
                    if col - 1 > -1:
                        if (row, col-1) not in visited:
                            visited.add((row, col-1))
                            nextlevel.append((row, col-1))  
                if found:
                    grid[i][j] = count
                    break
                if nextlevel:
                    queue.append(nextlevel)
                count += 1 
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    bfs(i, j)
