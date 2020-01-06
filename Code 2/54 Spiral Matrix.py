# 54. Spiral Matrix 
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order. 

For example,
 Given the following matrix: 
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5]. 
'''

#Array

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[]:
            return []
        res=[]
        left,right,up,down=0,len(matrix[0])-1,0,len(matrix)-1
        while True:
            if left<=right:
                for i in range(left,right+1):
                    res.append(matrix[up][i])
                up+=1
                if up>down:
                    break
            if up<=down:
                for i in range(up,down+1):
                    res.append(matrix[i][right])
                right-=1
                if left>right:
                    break
            if right>=left:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
                down-=1
                if up>down:
                    break                
            if down>=up:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
                if left>right:
                    break
        return res
                             
                    
        