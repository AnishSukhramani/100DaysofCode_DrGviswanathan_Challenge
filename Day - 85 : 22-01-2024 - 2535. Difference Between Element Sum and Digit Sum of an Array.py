class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum=0
        digitSum=0
        for i in nums:
            elementSum+=i
        for j in nums:
            s=str(j)
            for k in s:
                digitSum+=int(k)
        return abs(elementSum-digitSum)
