# 73. Set Matrix Zeroes 

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
Do it in place. 
'''

#Array

'Use firt row and first col to record the 0 setting for matrix[1:m][1:n];'
'Use Two indicator to record the 0 setting of first row/col'

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None
        
        firstRow,firstCol=1,1
        for j in range(len(matrix[0])):
            if matrix[0][j]==0:
                firstRow=0
                break
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                firstCol=0
                break

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(1,len(matrix)):
            if  matrix[i][0]==0:
                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0
        for j in range(1,len(matrix[0])):
            if matrix[0][j]==0:
                for i in range(1,len(matrix)):
                    matrix[i][j]=0
        if firstCol==0:
            for i in range(0,len(matrix)):
                 matrix[i][0]=0
        if firstRow==0:
            for j in range(0,len(matrix[0])):
                 matrix[0][j]=0            