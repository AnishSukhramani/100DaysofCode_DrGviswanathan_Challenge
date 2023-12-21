class Solution(object):
    def smallestEvenMultiple(self, n):
        maxNum=max(n,2)
        while(True):
            if (maxNum%n==0 and maxNum%2==0):
                break
            maxNum+=1
        return maxNum
