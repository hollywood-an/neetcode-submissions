class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        def backtrack(path, i, j):
            if "".join(path) == word:
                #print("hi")
                nonlocal result
                result = True
                #print(result)
                return 
            for l in range(len(word) - 1):
                if i+1 == len(board) or j+1 == len(board[0]):
                    continue
                path.append(board[i+1][j])
                backtrack(path, i+1, j)
                path.pop()
                path.append(board[i][j+1]) 
                backtrack(path, i, j+1)
                path.pop()
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack([board[i][j]], i, j)
                print(result)

        return result
        