#61. Rotate List 
 
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
 Given 1->2->3->4->5->NULL and k = 2,
 return 4->5->1->2->3->NULL.
'''

#Linked List, Two Pointers 

class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def ratteRight(self,head,k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head==None:
            return head
            
        cntNode=head
        size=0
        while cntNode!=None:
            size+=1
            cntNode=cntNode.next
        k=k%size
            
        if k==0:
            return head
        
        pseudo=ListNode(0)
        pseudo.next=head
        ptr1=pseudo
        ptr2=pseudo
        
        for i in range(k):
            ptr2=ptr2.next
        
        while ptr2.next:
            ptr2=ptr2.next
            ptr1=ptr1.next
        
        res=ptr1.next
        ptr2.next=head
        ptr1.next=None
        
        return res
        
        
        