# 9. Palindrome Number 


'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x==0:
            return True
        
        origin=x
        reverse=0

        while x>0:
            reverse=reverse*10+x%10
            x=x/10
        if reverse==origin:
            return True
        
        return False

'''
Idea:
Get the reverse of the number
Check if reverse=original
'''
