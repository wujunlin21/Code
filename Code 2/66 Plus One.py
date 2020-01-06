# 66 Plus One


'''
Given a non-negative integer represented 
as a non-empty array of digits, 
plus one to the integer.

You may assume the integer do not contain any leading zero,
 except the number 0 itself.

The digits are stored such that 
the most significant digit is at the head of the list.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        index=len(digits)-1
        
        mySum=digits[index]+1
        carry=mySum/10
        digits[index]=mySum%10
        while carry>0:
            index=index-1
            if index<0:
                return [carry]+digits
            mySum=digits[index]+carry
            carry=mySum/10
            digits[index]=mySum%10
        return digits
            
