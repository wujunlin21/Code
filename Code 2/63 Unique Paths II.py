# 63. Unique Paths II 
 
"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. 
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.
"""


#Array, Dynamic Programming 

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        mp=obstacleGrid
        for i in range(len(mp)):
            for j in range(len(mp[0])):
                if i==0 and j==0:
                    mp[i][j]=1-mp[i][j]
                elif i==0:
                    if mp[i][j]==1:
                        mp[i][j]=0
                    else:
                        mp[i][j]=mp[i][j-1]
                elif j==0:
                    if mp[i][j]==1:
                        mp[i][j]=0
                    else:
                        mp[i][j]=mp[i-1][j]       
                else:
                    if mp[i][j]==1:
                        mp[i][j]=0
                    else:
                        mp[i][j]=mp[i-1][j]+mp[i][j-1]
        return mp[-1][-1]
                    
