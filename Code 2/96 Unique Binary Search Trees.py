# 96. Unique Binary Search Trees 

'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
 Given n = 3, there are a total of 5 unique BST's. 
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

#Tree, Dynamic Programming 


class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt=[None for i in range(n+1)]
        opt[0]=1
        for i in range(1,n+1):
            aSum=0
            for j in range(0,i):
                aSum+=opt[j]*opt[i-j-1]
            opt[i]=aSum
        return opt[n]

'''
DP:
OPT(0)=1, OPT(1)=1,OPT(2)=2,OPT(3)=5
OPT(n)=OPT(0)*OPT(n-1)+OPT(1)*OPT(n-2)+...+OPT(n-1)*OPT(0)

given number n, root value can be 1..n. 
for root value i, left subtree contains range(1,i) i-1 numbers,
right subtree contains range(i+1,n+1) n-i number ,
so for a given root value i, there's OPT(i-1)*OPT(n-i) different trees
'''