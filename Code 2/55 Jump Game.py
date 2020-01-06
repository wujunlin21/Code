#55. Jump Game 

'''
Given an array of non-negative integers, 
you are initially positioned at the first index of the array. 
Each element in the array represents your maximum jump length at that position. 
Determine if you are able to reach the last index. 

For example:
 A = [2,3,1,1,4], return true. 
 A = [3,2,1,0,4], return false. 
'''

#Array, Greedy


class Solution(object):
    def canJump(self,nums):
       p=0
       ans=0
       for item in nums:
           if (ans<p):
               return False
           ans=max(ans,p+item)           
           p+=1
       return True

    
'''
1. Condition for reaching position i: maxIndex>=i
2. When at position i, maxIndex=max(maxIndex,i+A[i])
3. Condition for reaching n-1 position: maxIndex>=n-1
'''