# 64. Minimum Path Sum 

'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        results=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    results[i][j]=grid[i][j]
                elif i==0:
                    results[i][j]=results[i][j-1]+grid[i][j]
                elif j==0:
                    results[i][j]=results[i-1][j]+grid[i][j]
                else:
                    results[i][j]=min(results[i][j-1],results[i-1][j])+grid[i][j]

        return results[-1][-1]