#129. Sum Root to Leaf Numbers 
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example, 
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
 The root-to-leaf path 1->3 represents the number 13. 

Return the sum = 12 + 13 = 25. 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.sums=0
        self.dfs(root,root.val)
        return self.sums
    def dfs(self,root,aSum):
        if root.left==None and root.right==None:
            self.sums+=aSum
        if root.right!=None:
            self.dfs(root.right,aSum*10+root.right.val)
        if root.left!=None:
            self.dfs(root.left,aSum*10+root.left.val)
        
    
        