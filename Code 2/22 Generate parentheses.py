#22. Generate Parentheses 

'''
Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses. 

For example, given n = 3, a solution set is: 
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

#Backtracking, String 


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result=[]
        if n==0:
            return result

        oN,cN=n,n
        self.dfs(oN,cN,"",result)
        return result

    def dfs(self,oN,cN,aStr,result):
        if oN==0 and cN==0:
            result.append(aStr)
            return None
        if oN==cN:
            self.dfs(oN-1,cN,aStr+"(",result)
            return None
        if oN>0:
            self.dfs(oN-1,cN,aStr+"(",result)
        if cN>0:
            self.dfs(oN,cN-1,aStr+")",result)
            
