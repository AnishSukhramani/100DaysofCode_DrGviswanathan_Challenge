class Solution(object):
    def countPairs(self, nums, target):
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i]+nums[j]<target:
                    count+=1
        return count
