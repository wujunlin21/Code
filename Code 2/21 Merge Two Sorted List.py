#21. Merge Two Sorted Lists 

'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''

class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return None
        elif l1==None:
            return l2
        elif l2==None:
            return l1

        if l1.val<=l2.val:
            head=l1
            ptr=l1
            l1=l1.next
            
        else:
            head=l2
            ptr=l2
            l2=l2.next


        while True:

            if l1==None:
                ptr.next=l2
                return head
            elif l2==None:
                ptr.next=l1
                return head
            elif l1.val<=l2.val:
                ptr.next=l1
                ptr=ptr.next
                l1=l1.next
            else:
                ptr.next=l2
                ptr=ptr.next
                l2=l2.next

                

  
