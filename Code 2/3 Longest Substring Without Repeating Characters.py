#3. Longest Substring Without Repeating Characters

'''
Given a string,
find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
'''

#Hash Table, Two Pointers, String

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
            
        res=0
        hash={}
        l=0
        for i in range(len(s)):
            if s[i] in hash and hash[s[i]]>=l:
                 if r-l+1>res:
                     res=r-l+1
                 l=hash[s[i]]+1
                 hash[s[i]]=i
                 r=i
            else:
                hash[s[i]]=i
                r=i
        if r-l+1>res:
            res=r-l+1
        return res



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        soln=0
        start=0
        sDic={}
        for i in range(len(s)):
            if s[i] in sDic and sDic[s[i]]>=start:
                soln=max(soln,i-start)
                start=sDic[s[i]]+1
                sDic[s[i]]=i
            else:
                sDic[s[i]]=i
                
        soln=max(soln,i-start+1)
        return soln
                
