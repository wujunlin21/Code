#16. 3Sum Closest 

'''
Given an array S of n integers,
find three integers in S such that the sum is closest to a given number,target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example,
given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2.
(-1 + 2 + 1 = 2).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res=None

        if not nums:
            return res

        nums.sort()

        for i in range(len(nums)-2):
            if i and nums[i]==nums[i-1]:
                continue

            l=i+1
            r=len(nums)-1
            while l<r:
                approx=nums[i]+nums[l]+nums[r]
                if approx==target:
                    return approx
                if res==None or abs(target-approx)<abs(res-target):
                    res=approx
                if target>approx:
                    l+=1
                else:
                    r-=1
            
        return res
                

        
