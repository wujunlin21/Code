# 29. Divide Two Integers 


'''
Divide two integers without using multiplication, division and mod operator. 

If it is overflow, return MAX_INT. 
'''

#Math, Binary Search 

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        neg = (dividend>0 and divisor<0) or (dividend<0 and divisor>0)        
        a,b=abs(dividend),abs(divisor)
        
        MAX_INT=(1<<31)-1        
        if b==0:
            return MAX_INT
        
        if a<b:
            return 0
        
        ans,shift=0,31        
        while shift>=0:
            if a>= b<<shift:
                a-= b<<shift
                ans+= 1<<shift
            shift-= 1
        
        if ans>MAX_INT:
            return MAX_INT
        
        if neg:
            ans = -ans
        return ans
                
            