# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         arr=[]
#         for i in range(left, right+1):
#             ans=0
#             if i != 0 or i%10!=0:
#                 if "0" not in str(i):
#                     if len(str(i)) == 1:
#                         ans=1
#                     else:
#                         ans = 0
#                         for j in str(i):
#                             if i % int(j) == 0:
#                                 ans+=1
#             if len(str(i))==ans:
#                 arr.append(i)
#         return arr  

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1 ):
            ch=True
            for j in str(i):
                if j!='0':
                    if i%int(j)!=0:
                        ch=False
                else:
                    ch=False
                    break   
            if ch:
                res.append(i)
        return res
