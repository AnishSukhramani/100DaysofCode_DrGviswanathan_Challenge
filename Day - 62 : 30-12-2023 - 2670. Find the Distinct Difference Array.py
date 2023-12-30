class Solution(object):
    def distinctDifferenceArray(self, nums):
        answer=[]

        for i in range(len(nums)):
            l=[]
            r=[]
            for j in range(i+1):
                if nums[j] not in l:
                    l.append(nums[j])
            for k in range(i+1,len(nums)):
               if nums[k] not in r:
                    r.append(nums[k])
            answer.append(len(l)-len(r))
        return answer
