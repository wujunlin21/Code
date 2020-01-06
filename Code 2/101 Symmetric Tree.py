# 101. Symmetric Tree 

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric: 
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''

# Tree, Depth-first Search, Breadth-first Search 



#Method 1: Recusively (DFS)

# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root,root)
    
    def dfs(self,lr,rr):

        if lr==None and rr==None:
            return True
        elif lr==None or rr==None:
            return False
        else:
            if lr.val !=rr.val:
                return False                
        return self.dfs(lr.left,rr.right) and self.dfs(lr.right,rr.left)
        
        
#Method 2: iteratively (BFS)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        if not root:
            return True
        lQueue=deque([root.left])
        rQueue=deque([root.right])
        while len(lQueue)>0 and len(rQueue)>0:
            lNode=lQueue.popleft()
            rNode=rQueue.popleft()
            if lNode==None and rNode==None:
                continue
            elif lNode==None or rNode==None:
                return False
            elif lNode.val != rNode.val:
                return False
            else:
                lQueue.append(lNode.left)
                lQueue.append(lNode.right)
                rQueue.append(rNode.right)
                rQueue.append(rNode.left)                
        if len(lQueue)==0 and len(rQueue)==0:
            return True
        return False
'''Use two queue to BFS left and right subtrees
for left substree, put left child into queue first, then right child
for right substree, put right child into queue first'''
        