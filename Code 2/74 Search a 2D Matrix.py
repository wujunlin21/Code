# 74. Search a 2D Matrix 

'''
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
  •Integers in each row are sorted from left to right.
  •The first integer of each row is greater than the last integer of the previous row.

  
For example,
 Consider the following matrix: 
 [
   [1,   3,  5,  7],
   [10, 11, 16, 20],
   [23, 30, 34, 50]
 ]
 Given target = 3, return true.
'''

#Array, Binary Search 
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix==[[]]:
            return False
            
        col,row=len(matrix[0]),len(matrix)
        start,end=0,col*row-1
        while end-start>1:
            mid=(start+end)/2
            i,j=mid/col,mid%col
            val=matrix[i][j]
            if val>target:
                end=mid
            elif val<target:
                start=mid
            else:
                return True
                
        i,j=start/col,start%col 
        if matrix[i][j]==target:
            return True
        i,j=end/col,end%col 
        if matrix[i][j]==target:
            return True 
        return False

            