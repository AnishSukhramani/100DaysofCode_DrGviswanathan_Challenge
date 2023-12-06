# class Solution(object):
#     def runningSum(self, nums):
#         n=len(nums)
#         arr=[]
#         for i in range(n):
#             sum=nums[i]
#             for j in range(i):
#                 sum+=nums[j]
#             arr.append(sum)
#         return arr
class Solution(object):
    def runningSum(self, nums):
        n=len(nums)
        for i in range(1,n):
            nums[i]+=nums[i-1]
        return nums
