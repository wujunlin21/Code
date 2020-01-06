# 7 Reverse Integer

'''
Reverse digits of an integer.

Note:
 The input is assumed to be a 32-bit signed integer.
 Your function should return 0 when the reversed integer overflows. 

Example1: x = 123, return 321
Example2: x = -123, return -321 
'''

#Math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            sign=1
        else:
            sign=-1
            x=-x
        res=0
        
        while True:
            if x==0:
                if res>(1<<31)-1:
                    return 0
                return sign*res
            res=res*10+(x%10)
            x=x/10
                 

        
