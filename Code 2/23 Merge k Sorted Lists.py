#23. Merge k Sorted Lists 

'''
Merge k sorted linked lists
and return it as one sorted list.
Analyze and describe its complexity.
'''

#Divide and Conquer, Linked List, Heap

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#Heap  
#Time: O(nlogk)
#Space: O(k)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if lists==None:
            return None

        import heapq

        heap=[(node.val,node) for node in lists if node!=None]
        if heap==[]:
            return None
        heapq.heapify(heap)
        
        head=ListNode(0)
        ptr=head

        while heap:
            pop=heapq.heappop(heap)
            ptr.next=pop[1]
            ptr=ptr.next
            if pop[1].next==None:
                continue
            heapq.heappush(heap,(pop[1].next.val,pop[1].next))

        return head.next
            
            
            
 '''
Use heap:
put the first node of each linked list into heap,
pop out the min item,
put the next node of the min node into heap''' 

    


# Merge two by two solution. 
class Solution2(object): 
    def mergeKLists(self, lists): 
        """ 
        :type lists: List[ListNode] 
        :rtype: ListNode 
        """ 
        def mergeTwoLists(l1, l2): 
            curr = dummy = ListNode(0) 
            while l1 and l2: 
                if l1.val < l2.val: 
                    curr.next = l1 
                    l1 = l1.next 
                else: 
                     curr.next = l2 
                     l2 = l2.next 
                curr = curr.next 
            curr.next = l1 or l2 
            return dummy.next 

 
        if not lists: 
            return None 
        left, right = 0, len(lists) - 1; 
        while right > 0: 
            if left >= right: 
                left = 0 
            else: 
                lists[left] = mergeTwoLists(lists[left], lists[right]) 
                left += 1 
                right -= 1 
        return lists[0]  

    
