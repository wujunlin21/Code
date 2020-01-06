#35. Search Insert Position 

'''
Given a sorted array and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0 
'''

#Array, Binary Search 

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]:
            return 0
        
        l,r=0,len(nums)-1
        
        while l<=r:
                            
            m=(l+r)/2
            if nums[m]==target:
                return m
                
            if l==r:
                if target<nums[l]:
                    return l
                else:
                    return l+1
                    
            if nums[m]<target:
                l=m+1
            else:
                r=m
            
        
        
        