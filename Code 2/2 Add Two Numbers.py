#2. Add Two Numbers

'''
You are given two non-empty linked lists
representing two non-negative integers.
The digits are stored in reverse order
and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
342+465= 807
'''

# Linked List, Math

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        head=ListNode(0)
        curr=head
        carry=0

        while True:
            if l1 != None:
                carry += l1.val
                l1=l1.next
            if l2 != None:
                carry += l2.val
                l2=l2.next
            curr.val=carry%10
            carry=carry/10

            if l1!=None or l2!=None or carry !=0:
                curr.next=ListNode(0)
                curr=curr.next
            else:
                break

        return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pseudo=ListNode(0)
        result=pseudo
        carry=0
        while l1 or l2 or carry:        
            if l1==None:
                a=0
            else:
                a=l1.val
                l1=l1.next
            if l2==None:
                b=0
            else:
                b=l2.val 
                l2=l2.next                
            aSum=a+b+carry    
            remain=aSum%10 
            carry=aSum//10
            result.next=ListNode(remain)
            result=result.next
        return pseudo.next            
