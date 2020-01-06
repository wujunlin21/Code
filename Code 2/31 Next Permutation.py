# 31 Next Permutation 
 
'''
Implement next permutation,
which rearranges numbers into the lexicographically
next greater permutation of numbers. 

If such arrangement is not possible,
it must rearrange it as the lowest possible order
(ie, sorted in ascending order). 

The replacement must be in-place, do not allocate extra memory. 

e.g.
Inputs are in the left-hand column
and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
'''


#My Solution
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for index in range(len(nums)-1,0,-1):
            if nums[index]>nums[index-1]:
                #nums[index],nums[index-1]=nums[index-1],nums[index]
                j=index-1
                for k in range(len(nums)-1,j,-1):
                    if nums[k]>nums[j]:
                        nums[k],nums[j]=nums[j],nums[k]
                        break

                m=index
                l=len(nums)-1
                while m<l:
                    nums[m],nums[l]=nums[l],nums[m]
                    m+=1
                    l-=1
                return None

        m=0
        l=len(nums)-1
        while m<l:
            nums[m],nums[l]=nums[l],nums[m]
            m+=1
            l-=1
        return None



#JiuZhang Solution
class Solution2(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        
        for i in range(len(nums)-2, -1, -1):            
            if nums[i] < nums[i+1]:
                break
        else:
            nums.reverse()
            return None

        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        for j in range(0, (len(nums) - i)//2):
            nums[i+j+1], nums[len(nums)-j-1] = nums[len(nums)-j-1], nums[i+j+1]
        return None
