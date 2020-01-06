# 17. Letter Combinations of a Phone Number

'''
Given a digit string,
return all possible letter combinations that the number could represent. 
A mapping of digit to letters (just like on the telephone buttons)is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

#Backtracking, String 


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """


        
        self.DToL={"2":["a","b",'c'],"3":["d","e",'f'],"4":["g","h",'i'],\
              "5":["j","k",'l'],"6":["m","n",'o'],"7":["p","q",'r','s'],\
              "8":["t","u",'v'],"9":["w","x",'y','z']}

        result=[]

        if digits=="":
            return result

        self.dfs(digits,"",result)

        return result


    def dfs(self,digits,aStr,result):
        if digits=="":
            result.append(aStr)         
        elif digits[0] in self.DToL:
            for letter in self.DToL[digits[0]]:
                self.dfs(digits[1:],aStr+letter,result)
        else:
            self.dfs(digits[1:],aStr,result)
