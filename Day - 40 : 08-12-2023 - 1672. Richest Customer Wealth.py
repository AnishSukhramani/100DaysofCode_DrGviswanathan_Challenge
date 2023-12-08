class Solution(object):
    def maximumWealth(self, accounts):
        arr=[]
        for i in range(len(accounts)):
            wealth=0
            for j in range(len(accounts[i])):
                wealth+=accounts[i][j]
                arr.append(wealth)
        arr.sort(reverse=True)
        return arr[0]
        
