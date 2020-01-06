# 111. Minimum Depth of Binary Tree 

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.'''

#Tree, Depth-first Search, Breadth-first Search 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth( root.right ) + 1
        if root.left != None and root.right == None:
            return self.minDepth( root.left ) + 1
        return min( self.minDepth( root.left ), self.minDepth( root.right ) ) + 1
        
'''
1. if root=None: 0
2. root only has left or right subtree，return the min depeth of left or right subtree +1
3. if root has both left and right subtrees, than return the smaller of minDepth of the two subtrees +1。
'''
