class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        def backtrack(path, i, j):
            if "".join(path) == word:
                nonlocal result
                result = True
                return 
            if len(path) == len(word):
                return
            if i >= len(board):
                return
            if i < 0:
                return
            if j < 0:
                return
            if j >= len(board[0]):
                return
            path.append(board[i][j])
            backtrack(path, i+1, j)
            backtrack(path, i-1, j)
            backtrack(path, i, j-1)
            backtrack(path, i, j+1)
            path.pop()
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack([], i, j)

        return result
        