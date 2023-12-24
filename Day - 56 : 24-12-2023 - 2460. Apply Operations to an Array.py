class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]*=2
                nums[i]*=0
        for j in range(len(nums)):
            if nums[j]==0:
                nums.remove(nums[j])
                nums.append(0)
        return nums
