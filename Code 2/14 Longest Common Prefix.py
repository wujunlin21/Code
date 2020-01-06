#14. Longest Common Prefix

'''
Write a function to find the longest common prefix string
amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''

#String

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        i=0
        while i<len(strs[0]):
            s=strs[0][i]
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=s:
                    return strs[0][0:i]
            i+=1
        return strs[0][0:i]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        if len(strs)==1:
            return strs[0]

        i=0
        while True:
            for j in range(0,len(strs)-1):
                if i>=len(strs[j]) or i>=len(strs[j+1]) or strs[j][i]!=strs[j+1][i]:
                    return strs[0][0:i]
            i+=1

'''
For method 2, the inner for loop cannot loop if through len(strs)=1,
thus add len=1 contition at begining
'''
