import itertools
import math

def isValidSudoku(board):

    Matrix = [[],[],[],[],[],[],[],[],[]]
    Row = [[],[],[],[],[],[],[],[],[]]
    Column = [[],[],[],[],[],[],[],[],[]]

    ###每一行元素
    for i in range(9):
        for e in board[i]:
            if e != ".":
                Row[i].append(e)
    print("Row:",Row)
    ###每一列元素
    for i in range(9):
        for j in range(9):
            if board[j][i] != ".":
                Column[i].append(board[j][i])
    print("Column:",Column)

    for i in range(9):
        for j in range(9):
            if 0<=i<=2 and 0<=j<=2 and board[i][j]!=".":
                Matrix[0].append(board[i][j])
            if 0<=i<=2 and 3<=j<=5 and board[i][j]!=".":
                Matrix[1].append(board[i][j])
            if 0<=i<=2 and 6<=j<=8 and board[i][j]!=".":
                Matrix[2].append(board[i][j])
            if 3<=i<=5 and 0<=j<=2 and board[i][j]!=".":
                Matrix[3].append(board[i][j])
            if 3<=i<=5 and 3<=j<=5 and board[i][j]!=".":
                Matrix[4].append(board[i][j])
            if 3<=i<=5 and 6<=j<=8 and board[i][j]!=".":
                Matrix[5].append(board[i][j])
            if 6<=i<=8 and 0<=j<=2 and board[i][j]!=".":
                Matrix[6].append(board[i][j])
            if 6<=i<=8 and 3<=j<=5 and board[i][j]!=".":
                Matrix[7].append(board[i][j])
            if 6<=i<=8 and 6<=j<=8 and board[i][j]!=".":
                Matrix[8].append(board[i][j])
    print("Matrix:", Matrix)
    ###9个小矩阵的判重
    for i in range(9):
        if len(Matrix[i]) != len(set(Matrix[i])):
            print("false")
            return False
    ###9行的判重
    for i in range(9):
        if len(Row[i]) != len(set(Row[i])):
            print("false")
            return False
    ###9列的判重
    for i in range(9):
        if len(Column[i]) != len(set(Column[i])):
            print("false")
            return False
    return True





if __name__ == '__main__':
    isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])