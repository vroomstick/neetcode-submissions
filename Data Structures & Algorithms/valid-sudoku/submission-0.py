class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check duplicate row

        for i in range(len(board)):
            key = {str(k + 1) for k in range(9)}

            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in key:
                    key.remove(board[i][j])
                else:
                    return False

        # check duplicate column

        for i in range(len(board)):
            key = {str(k + 1) for k in range(9)}
            col = [row[i] for row in board]

            for j in range(len(col)):
                if col[j] == ".":
                    continue
                if col[j] in key:
                    key.remove(col[j])
                else:
                    return False

        #check 3x3 
        for i in range(0, 9, 3):          # top-left row
            for j in range(0, 9, 3):      # top-left col
                key = {str(k + 1) for k in range(9)}
                for r in range(i, i + 3):      # rows within box
                    for c in range(j, j + 3):  # cols within box
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in key:
                            key.remove(board[r][c])
                        else:
                            return False

        return True




                        




            
            

        