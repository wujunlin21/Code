# 62. Unique Paths 
 
'''
A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
'''

#Array Dynamic Programming 


#bottom up (f(m,n)=f(m-1,n)+f(m,n-1))
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if m<=0 or n<=0:
            return None
        if m==1 or n==1:
            return 1
        
        
        results=[[1 for i in range(n)]]+[[1] for i in range(m-1)]
        i=2
        while i<=m:
            j=2
            while j<=n:
                results[i-1].append(results[i-1][j-2]+results[i-2][j-1])
                j+=1
            i+=1
        
        return results[-1][-1]

        
        

if __name__=='__main__':
    ins=Solution()
    print ins.uniquePaths(4,3)
                 
        