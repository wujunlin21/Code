#20. Valid Parentheses 

'''
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s=="":
            return True
        
        stack=[]

        for i in s:
            if i in {'(','{','['}:
                stack.append(i)
                print i
            else:
                if len(stack)==0:
                    return False
                if i==')':
                    if stack.pop() != '(':
                        return False
                elif i==']':
                    if stack.pop() != '[':
                        return False
                else:
                    if stack.pop() !='{':
                        return False

        if len(stack)==0:
            return True       
        else:
            return False
        
        
