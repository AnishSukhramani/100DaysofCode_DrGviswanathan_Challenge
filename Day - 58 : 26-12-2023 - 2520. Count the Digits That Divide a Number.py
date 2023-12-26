# class Solution:
#     def countDigits(self, num: int) -> int:
#         str_num=str(num)
#         count=0
#         for i in range(len(str_num)):
#             temp=int(str_num[i])
#             if num%temp==0:
#                 count+=1
#         return count
class Solution:
    def countDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return 1
        else:
            ans = 0
            for i in str(num):
                if num % int(i) == 0:
                    ans += 1
            return ans
