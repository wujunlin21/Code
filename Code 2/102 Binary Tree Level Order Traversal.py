# 102. Binary Tree Level Order Traversal 
 
"""
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
 Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[ [3],
  [9,20],
  [15,7]  ]
"""

#Breadth-first Search 

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res=[]
        curL=[root]
        while curL:
            nextL=[]
            vals=[]
            for node in curL:
                vals.append(node.val)
                if node.left != None:
                    nextL.append(node.left)
                if node.right != None:
                    nextL.append(node.right)                
            curL=nextL
            res.append(vals)

        return res
        

#recursion
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """  
        res=[]
        self.preorder(root,0,res)
        return res
        
    def preorder(self,root,level,res):
        if root:
            if len(res)<level+1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left,level+1,res)
            self.preorder(root.right,level+1,res)
            
        