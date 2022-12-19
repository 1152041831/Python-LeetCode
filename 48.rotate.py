import itertools
import math

import numpy as np


def rotate(matrix):
    n = len(matrix[0])

    #先转置matrix
    for i in range(n):
        for j in range(i):
            temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp
    #再调换每一列的位置,沿着中心对称
    for i in range(n):
        for j in range(n//2):
            temp = matrix[i][j]
            print("temp:",temp)
            print(f"{i, j}=>{i, n - 1 - j}")
            print(f"{matrix[i][j]}=>{matrix[i][n-1-j]}")
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n - 1 - j] = temp
            print(f"{i,j}=>{i,n-1-j}")
    print(np.array(matrix))

    return matrix




if __name__ == '__main__':
    rotate([[1,2,3],[4,5,6],[7,8,9]])