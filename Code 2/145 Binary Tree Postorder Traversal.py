# 145 Binary Tree Postorder Traversal

'''
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
 Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
return [3,2,1]. 
'''
#(a) Inorder (Left, Root, Right) : 4 2 5 1 3
#(b) Preorder (Root, Left, Right) : 1 2 4 5 3
#(c) Postorder (Left, Right, Root) : 4 5 2 3 1
#Tree, Stack 


#PostOrder:left,root,right

#Method 1: iteration
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        res=[]
        stack = []
        pre = None
        stack.append(root)
        while stack:
            curr = stack[len(stack) - 1]
            if (curr.left == None and curr.right == None) or (pre and (pre == curr.left or pre == curr.right)):
                res.append(curr.val)
                stack.pop()
                pre = curr
            else:
                if curr.right: stack.append(curr.right)
                if curr.left: stack.append(curr.left)
        return res

'''
e.g.　　　　　　　　　　　1
 　　　　　　　　　　　　/　　\
　　　　　　　　　　　　2　　　　3
　　　　　　　　　　　　　　　　/　\
　　　　　　　　　　　　　　　 4　　5
1. put root into stack. If root has child, put its child into stack,
   right child firt, then left child. 
   while the last node in stack has child, put the child(s) into stack
   right child firt, then left child.      
   {1,3,2}
2. if the last node in stack doesn't have child, 
   or the node is the parent of pre,
    pop the node, prev point at the node
    {1,3}, pre->2
3. while the last node in stack has child, put the child(s) into stack
   right child firt, then left child. 
   {1,3,5,4}
4.  the last node in stack doesn't have child, 
    pop the node, prev point at the node
    {1,3}, pre->5
5. the last node is the parent of pre,
    pop the node, prev point at the node
    {1},pre->3; {},pre->1
'''

        
        
        
        
#Method 2: recusive
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res=[]
        self.recursive(root,res)
        return res
        
    def recursive(self,root,res):
        if root.left:
            self.recursive(root.left,res)
        if root.right:
            self.recursive(root.right,res)
        res.append(root.val)