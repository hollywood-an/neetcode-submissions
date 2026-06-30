class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        paths = []
        def dfs(i, j):
            stack = [(i, j)]
            path = []
            while stack:
                n = stack.pop()
                if n not in visited:
                    visited.add(n)
                    n_i, n_j = n
                    if n_i == 0 or n_j == 0 or n_i == len(board)-1 or n_j == len(board[0])-1:
                        if board[n_i][n_j] == "X":
                            paths.append(path)
                        return 
                    for x,y in directions:
                        stack.append((n_i+x, n_j+y))
                path.append((i,j))

        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == "O":
                    dfs(i, j)

        print(paths)
        for path in paths:
            for i, j in path:
                board[i][j] = "X"