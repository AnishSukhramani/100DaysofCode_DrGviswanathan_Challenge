class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sr_nums=sorted(nums)
        arr=[]
        for i in range(len(sr_nums)):
            if sr_nums[i] == target:
                arr.append(i)
        return arr
