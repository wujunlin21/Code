#83. Remove Duplicates from Sorted List 


'''
Given a sorted linked list, 
delete all duplicates such that each element appear only once. 

For example,
 Given 1->1->2, return 1->2.
 Given 1->1->2->3->3, return 1->2->3. 
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head==None:
            return head
        
        ptr=head
        post=ptr.next
        
        while True:
            if post==None:
                ptr.next=None
                return head
            if post.val != ptr.val:
                ptr.next=post
                ptr=ptr.next
                post=ptr.next
            else:
                post=post.next
        