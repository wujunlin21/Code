#130. Surrounded Regions 
'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region. 

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be: 
X X X X
X X X X
X X X X
X O X X
'''

#BFS, Union Find

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def helper(i,j):
            if x<0 


            
        def dfs(i,j):
            if board[i][j]=='O':
                queue.append((i,j))
            while queue:
                curr=queue.popleft()
                x,y=curr[0], curr[1]
                helper(x-1,y)
                helper(x+1,y)
                helper(x,y+1)
                helper(x,y-1)

                
                
        if board==None:
            return
        import collections
        queue=collections.deque([])
        m=len(board)
        n=len(board[0])
        for index in range(n):
            dfs(0,index)
            dfs(m-1,index)
        for index in range(m):
            dfs(index,0)
            dfs(index,n-1)

            
        