# 95. Unique Binary Search Trees II 

'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
 Given n = 3, your program should return all 5 unique BST's shown below. 
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


#Tree, DFS

class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        

class Solution(object):
    def generateTrees(self,n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        return self.dfs(1,n)
    
    def dfs(self,start,end):
        if start>end:
            return [None]
        res=[]
        for rootval in range(start,end+1):
            leftTree=self.dfs(start,rootval-1)
            rightTree=self.dfs(rootval+1,end)
            for i in leftTree:
                for j in rightTree:
                    root=TreeNode(rootval)
                    root.left=i
                    root.right=j
                    res.append(root)
        return res
        