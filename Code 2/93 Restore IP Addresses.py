# 93. Restore IP Addresses 

'''
Given a string containing only digits, 
restore it by returning all possible valid IP address combinations.

For example:
 Given "25525511135", 
 return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 
'''

#Backtracking, String 

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        self.dfs(s, 0, res, '')
        return res
    
    def dfs(self,s, sub, res, ip):
        if sub == 4:                # should be 4 parts
            if s == '':
                res.append(ip[1:])  # remove first '.'
            return
        for i in range(1,4):
            if i<=len(s):
                if int(s[:i])<=255:
                    self.dfs(s[i:],sub+1,res,ip+'.'+s[:i])
                if s[0]=='0': break  # make sure that res just can be '0.0.0.0' and remove like '00'
        
                

        
        

        
'''
A valid IP address consist of 4 digits, each between [0,255].
Two or three digit combination cannot begin with 0:
    (i.e 001 X, 01 X, 1 OK)
'''

