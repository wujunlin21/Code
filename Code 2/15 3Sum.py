#15 3Sum

'''
Given an array S of n integers,
are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

#Array, Two Pointer

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res=[]

        for i in range(len(nums)-2):
            if i and nums[i]==nums[i-1]:
                continue

            target=0-nums[i]
            
            l=i+1
            r=len(nums)-1

            while l<r:
                if nums[l]+nums[r]==target:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return res


            
'''
3 Sum = 0 , remove duplicate:
sorted list
use two pointer begining from two ends of the list
if two solution ai,aj and ak,al then i<k j>l or i>k j<l
Now O(N) to solve 2 sum
3 Sum is to enumerate the first element (O(N^2))
if meet same value for a pointer, skip that value
'''
            
