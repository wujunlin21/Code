# 46. Permutations

'''
Given a collection of distinct numbers, return all possible permutations. 

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return 
        res=[]
        self.dfs([],nums,res)
        return res
    
    def dfs(self,alist,nums,res):
        if nums==[]:
            res.append(alist)
            return None
        for i in range(len(nums)):
            self.dfs(alist+[nums[i]],nums[:i]+nums[i+1:],res)
            
            
        