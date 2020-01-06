#5. Longest Palindromic Substring

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example: 
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

#string


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res,lAns,rAns=0,0,0
        length=len(s)
            
        for i in range(1,length*2):

            if i%2==1:
                left=i/2
                right=left

            elif i%2==0:
                left=i/2-1
                right=left+1

            while left>=0 and right<length and s[left]==s[right]:
                left-=1
                right+=1

            left=left+1
            right=right-1
            if right-left+1>res:
                res,lAns,rAns=right-left+1,left,right

        return s[lAns:rAns+1]
                
            
