# 134. Gas Station 

'''
There are N gas stations along a circular route, 
where the amount of gas at station i is gas[i]. 

You have a car with an unlimited gas tank 
and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations. 

Return the starting gas station's index if you can travel around the circuit once, 
otherwise return -1. '''


#Greedy

'''
1.If sum(gas)>=sum(cost), there must be a solution
2.If from station i cannot reach station j (can only reach j-1), then any station between[i,j-1] cannot reach j
'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        diff = 0
        stationIndex = 0
        for i in range(n):
            if gas[i]+diff < cost[i]: stationIndex = i+1; diff = 0
            else: diff += gas[i]-cost[i]
        return stationIndex

