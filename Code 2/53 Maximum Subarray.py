# 53. Maximum Subarray

'''
Find the contiguous subarray within an array 
(containing at least one number) 
which has the largest sum. 

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 the contiguous subarray [4,-1,2,1] 
 has the largest sum = 6. 
'''



'''
dp

OPT(n)=
OPT(n-1)+an   if OPT(n-1)>0;
an            if OPT(n-1)<=0

OPT(n)=largest sum subarray ends with nth element
ans=max{opt(n)}
'''
class Solution(object):
    def maxSubArray(self,nums):
        
        res=nums[0]
        opt=nums[0]
        for num in nums[1:]:
            if opt>0:
                opt=opt+num
            else:
                opt=num
            res=max(res,opt)
        return res