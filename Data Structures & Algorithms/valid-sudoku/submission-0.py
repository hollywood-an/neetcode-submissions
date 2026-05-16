class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row = set()
            for j in range(len(i)):
                if i[j] in row and i[j] != ".":
                    return False
                row.add(i[j])

        for i in range(9):
            column = set()
            for j in range(9):
                if board[j][i] in column and board[j][i] != ".":
                    return False
                column.add(board[j][i])

        box1 = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] in box1 and board[i][j] != ".":
                    return False
                box1.add(board[i][j])

        box2 = set()
        for i in range(3):
            for j in range(3):
                if board[i+3][j] in box2 and board[i+3][j] != ".":
                    return False
                box2.add(board[i+3][j])

        box3 = set()
        for i in range(3):
            for j in range(3):
                if board[i+6][j] in box3 and board[i+6][j] != ".":
                    return False
                box3.add(board[i+6][j])
        box4 = set()
        for i in range(3):
            for j in range(3):
                if board[i][j+3] in box4 and board[i][j+3] != ".":
                    return False
                box4.add(board[i][j+3])
        box5 = set()
        for i in range(3):
            for j in range(3):
                if board[i+3][j+3] in box5 and board[i+3][j+3] != ".":
                    return False
                box5.add(board[i+3][j+3])
        box6 = set()
        for i in range(3):
            for j in range(3):
                if board[i+6][j+3] in box6 and board[i+6][j+3] != ".":
                    return False
                box6.add(board[i+6][j+3])
        box7 = set()
        for i in range(3):
            for j in range(3):
                if board[i][j+6] in box7 and board[i][j+6] != ".":
                    return False
                box7.add(board[i][j+6])
        box8 = set()
        for i in range(3):
            for j in range(3):
                if board[i+3][j+6] in box8 and board[i+3][j+6] != ".":
                    return False
                box8.add(board[i+3][j+6])
        box9 = set()
        for i in range(3):
            for j in range(3):
                if board[i+6][j+6] in box9 and board[i+6][j+6] != ".":
                    return False
                box9.add(board[i+6][j+6])
        return True
            