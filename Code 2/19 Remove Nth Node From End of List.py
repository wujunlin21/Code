#19. Remove Nth Node From End of List 

'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end,
   the linked list becomes 1->2->3->5.

Note:
 Given n will always be valid.
 Try to do this in one pass. 
'''

#Linked List, Two Pointers


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return None
        
        aux=ListNode(0)
        aux.next=head

        r=aux
        l=aux
        
        for i in range(n):
            r=r.next

        while r.next:
            r=r.next
            l=l.next

        if l.next.next == None:
            l.next=None
            return aux.next
        else:
            l.next=l.next.next
            return aux.next
        
        for i in range(n):
            r=r.next

        while r.next:
            r=r.next
            l=l.next

        if l.next.next == None:
            l.next=None
            return aux.next
        else:
            l.next=l.next.next
            return head.next


'''
Use two pointer,
the first pointer move to the nth node
The second and the first pointer move together
until the first pointer at the node
Now the second pointer is at the Nth node from the end of list
'''

        
        

        
            
            
