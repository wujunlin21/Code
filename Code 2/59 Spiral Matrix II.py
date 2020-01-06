# 59. Spiral Matrix II 

'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
 Given n = 3, 
You should return the following matrix: [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

#Array 

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        matrix=[[0 for i in range(n)] for j in range(n)]
        up,down,left,right=0,n-1,0,n-1
        count=0
        while True:
            if left<=right:
                for i in range(left,right+1):
                    count+=1
                    matrix[up][i]=count
                up+=1
                if up>down:
                    break
            if up<=down:
                for i in range(up,down+1):
                    count+=1
                    matrix[i][right]=count
                right-=1
                if left>right:
                    break
            if left<=right:
                for i in range(right,left-1,-1):
                    count+=1
                    matrix[down][i]=count
                down-=1
                if up>down:
                    break
            if up<=down:
                for i in range(down,up-1,-1):
                    count+=1
                    matrix[i][left]=count
                left+=1
                if left>right:
                    break    
        return matrix
                    