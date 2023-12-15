class Solution(object):
    def findMiddleIndex(self, nums):
        total = sum(nums)
        c=0
        for i in range(len(nums)):
            left_sum = 0
            for j in range(i):
                left_sum += nums[j]

            right_sum = total - nums[i] - left_sum
            if left_sum==right_sum:
                return i
                c=1
        if c==0:
            return -1
