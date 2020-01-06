#94. Binary Tree Inorder Traversal 
 
'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
 Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2]. '''
#Inorder (Left, Root, Right) : 4 2 5 1 3
#Inorder traversal gives nodes in non-decreasing order

#Tree, Hash Table, Stack 


#Method 1: Iterative
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution1(object):
    def inorderTraversal(self,root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        res=[]
        while root or stack:
            if root:
                stack.append(root)   
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res
    




#Method 2: Recursion
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution2(object):
    def inorderTraversal(self,root):
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
        if root.left!=None:
            self.recursive(root.left,res)
        res.append(root.val)
        if root.right != None:
            self.recursive(root.right,res)            
    