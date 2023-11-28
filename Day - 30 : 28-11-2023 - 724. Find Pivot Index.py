class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            l=0
            for j in range(i):
                l+=nums[j]
            r=sum(nums)-nums[i]-l
            if r==l:
                return i
        return -1
