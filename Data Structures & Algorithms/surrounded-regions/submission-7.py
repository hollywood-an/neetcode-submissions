class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i == rows or j == cols:
                return 
            if board[i][j] != "O" or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(1, rows-1):
            if board[i][0] == "O":
                dfs(i, 0)

        for i in range(1, cols-1):
            if board[0][i] == "O":
                dfs(0, i)

        for i in range(1, rows-1):
            if board[i][cols - 1] == "O":
                dfs(i, 0)

        for i in range(1, cols-1):
            if board[rows - 1][i] == "O":
                dfs(0, i)

        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if (i, j) not in visited:
                    board[i][j] = "X"        