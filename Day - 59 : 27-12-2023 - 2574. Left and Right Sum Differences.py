class Solution(object):
    def leftRightDifference(self, nums):
        total=sum(nums)
        answer=[]
        for i in range(len(nums)):
            left_sum=0
            for j in range(i):
                left_sum+=nums[j]

            right_sum=total-nums[i]-left_sum


            answer.append(abs(left_sum-right_sum))
        # print total
        return answer
