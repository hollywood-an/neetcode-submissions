class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        count = 0
        def backtrack(path, i, j, count):
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
            if board[i][j] != word[count]:
                return
            
            path.append(board[i][j])
            board[i][j] = "#"
            backtrack(path, i+1, j, count+1)
            backtrack(path, i-1, j, count+1)
            backtrack(path, i, j-1, count+1)
            backtrack(path, i, j+1, count+1)
            board[i][j] = path.pop()
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack([], i, j, 0)

        return result
        