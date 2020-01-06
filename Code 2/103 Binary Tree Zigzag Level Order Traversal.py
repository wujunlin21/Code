# 103. Binary Tree Zigzag Level Order Traversal 

'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
 Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#BFS
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        curL=[root]       
        direction=1
        while curL:
            nextL=[]
            temp=[]
            for node in curL:
                temp.append(node.val)
                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)
            if direction==1:
                res.append(temp)
                direction=-1
            else:
                temp.reverse()
                res.append(temp)
                direction=1
            curL=nextL
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
            if level%2==0:
                res[level].append(root.val)
            else:
                res[level].insert(0,root.val)
            self.preorder(root.left,level+1,res)
            self.preorder(root.right,level+1,res)
                
                
                