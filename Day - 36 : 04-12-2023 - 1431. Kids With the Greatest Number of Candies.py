class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        new_arr=sorted(candies,reverse=True)
        result=[]
        for i in candies:
            if i+extraCandies>=new_arr[0]:
                result.append(True)
            else:
                result.append(False)
        return result
        
