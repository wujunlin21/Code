#47. Permutations II 
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations. 

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res=[]
        self.dfs([],nums,res)
        return res
    
    def dfs(self,alist,nums,res):
        if nums==[]:
            res.append(alist)
        i=0
        while i<len(nums):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
                continue
            self.dfs(alist+[nums[i]],nums[:i]+nums[i+1:],res)
            i+=1
        
        