# 60. Permutation Sequence 

'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
 We get the following sequence (ie, for n = 3): 
1."123"
2."132"
3."213"
4."231"
5."312"
6."321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac=[1]                 #fac(0)=1
        for i in range(1,n):    #get fac(1) to fac(n-1)
            fac.append(fac[-1]*i)
        
        elegible=range(1,n+1)
        per=[]
        for i in range(n):
            index=(k-1)/fac[n-i-1]
            per.append(str(elegible[index]))
            del elegible[index]
            k=(k-1)%fac[n-i-1]+1
        
        res="".join(per)
        return res
            