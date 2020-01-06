#40. Combination Sum II 

'''
Given a collection of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T. 
Each number in C may only be used once in the combination. 

Note:
 •All numbers (including target) will be positive integers.
 •The solution set must not contain duplicate combinations.


For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
 A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        res=[]
        candidates.sort()
        self.dfs(candidates,target,[],res)
        return res
        
    def dfs(self,candidates,target,valList,res):
        if target==0:
            res.append(valList)
            return None
        if candidates==[]:
            return None
        for i in range(len(candidates)):
            if i>0 and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                return None
            self.dfs(candidates[i+1:],target-candidates[i],valList+[candidates[i]],res)
        