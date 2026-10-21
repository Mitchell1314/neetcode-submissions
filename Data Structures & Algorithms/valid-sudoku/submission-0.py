class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(0,row):
            visited = set()
            for j in range(0,col):
                if board[i][j] not in visited and board[i][j] != ".":
                    visited.add(board[i][j])
                elif board[i][j] in visited:
                    return False
        for i in range(0,col):
            visited = set()
            for j in range(0,row):
                if board[j][i] not in visited and board[j][i] != ".":
                    visited.add(board[j][i])
                elif board[j][i] in visited:
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.check_box_valid(i, j, board):
                    return False
        return True
    def check_box_valid(self,i, j, board):
            visited = set()
            for k in range(0, 3):
                for l in range(0, 3):
                    if board[k + i][j + l] not in visited and board[k + i][j + l] !=".":
                        visited.add(board[k + i][j + l])
                    elif board[k + i][j + l] in visited:
                        return False
            return True