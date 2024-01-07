class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=-1
        end=-1
        arr=[]
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        if len(arr)>0:
            if arr[0]>=0:
                start=arr[0]
            if arr[len(arr)-1]>=0:
                end=arr[len(arr)-1]
        return [start,end]
        
