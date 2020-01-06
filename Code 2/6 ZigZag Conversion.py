#5. ZigZag Conversion

'''
The string "PAYPALISHIRING" is written in a zigzag pattern
on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''

#string


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans=''
        loop=numRows+numRows-2
        if numRows==1:
            loop=1
        for i in range(numRows):
            j=i
            inter=1
            while j<len(s):
                ans=ans+s[j]
                if i==0 or i==numRows-1:
                    j=j+loop
                elif inter==1:
                    j=j+loop-i*2
                    inter=0
                else:
                    j=j+i*2
                    inter=1
        return ans                
            
                
            
