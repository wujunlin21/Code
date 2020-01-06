# 69 Sqrt(x) 

'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        start=1
        end=x
        while end-start>1:
            mid=(start+end)/2
            if mid*mid>x:
                end=mid
            elif mid*mid<x:
                start=mid
            else:
                return mid
        if end*end<=x:
            return end
        return start