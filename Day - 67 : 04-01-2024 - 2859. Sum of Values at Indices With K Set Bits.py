class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            total_set_bits=bin(i).count("1")
            if total_set_bits==k:
                c+=nums[i]
        return c
