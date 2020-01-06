# 28 Implement strStr()

'''
Implement strStr(). 
Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        lenHay=len(haystack)
        lenNeed=len(needle)

        for i in range(lenHay-lenNeed+1):

            for j in range(lenNeed):
                if haystack[i+j]!=needle[j]:
                    break
                if j==lenNeed-1:
                    return i
        
        return -1
