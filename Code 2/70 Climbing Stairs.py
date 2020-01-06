#70. Climbing Stairs 

'''
You are climbing a stair case. 
It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top? 

Note: Given n will be a positive integer. 
'''

'''
DP

OPT(n)=OPT(n-1)+OPT(n-2)
'''

#Top down
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        self.result=[None for i in range(n)]
        self.result[0]=1
        self.result[1]=2
        return self.helper(n)
    
    def helper(self,n):
        if self.result[n-1] != None:
            return self.result[n-1]
        res=self.helper(n-1)+self.helper(n-2)
        self.result[n-1]=res
        return res



#Bottom Up        
class Solution(object):
    def climbStairs(self,n):
        if n<=2:
            return n
        result=[1,2]
        for i in range(3,n+1):
            result.append(result[-1]+result[-2])
        return result[-1]

