#24. Swap Nodes in Pairs

'''
Given a linked list,
swap every two adjacent nodes and return its head. 

For example,
 Given 1->2->3->4,
 you should return the list as 2->1->4->3. 

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed. 
'''

#Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        elif head.next == None:
            return head
        else:
            temp=ListNode(0)
            res=temp
            pre=head
            post=head.next
            

        while True:
            temp.next=post
            pre.next=post.next
            post.next=pre
            temp=pre
            
            pre=pre.next
            if pre == None:
                return res.next       
            post=pre.next
            if post==None:
                temp.next=pre
                return res.next

            
            
            
            
