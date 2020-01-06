# 144. Binary Tree Preorder Traversal 

'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
 Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3]. 
'''

# Tree, Stack 

#PreOrder: Root, Left, Right

#Method1: iterative
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def preorderTraversal(self,root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res=[]
        stack=[root]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
            


#Method2: recursive
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def preorderTraversal(self,root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        res=[]
        self.recursive(root,res)
        return res
        
    def recursive(self,root,res):
        res.append(root.val)
        if root.left != None:
            self.recursive(root.left,res)
        if root.right != None:
            self.recursive(root.right,res) 



