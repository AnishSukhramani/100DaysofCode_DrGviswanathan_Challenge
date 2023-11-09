class Solution(object):
    def lengthOfLastWord(self, s):
        return (len(s.strip().split(" ")[-1]))
        # if len(s)==1:
        #     return 1
        # else:
        #     arr=s.split(" ")
        #     n=len(arr)
        #     temp=arr[n-1]
        #     ans=[]
        #     for j in range(0,len(arr)):
        #         count=0
        #         x=arr[j]
        #         for i in range(0,len(x)):
        #             count=i
        #         ans.append(count+1)
        #     ans.reverse()
        #     for k in range(0,len(ans)+1):
        #         if ans[k]!=1:
        #             return ans[k]
        #             break
# The given Python class `Solution` contains a method `lengthOfLastWord` that takes a string `s` as input and returns the length of the last word in the string. The method uses the `strip()` method to remove leading and trailing whitespaces, then `split(" ")` is used to split the string into a list of words based on spaces. Finally, the length of the last word in the list is returned. The commented-out code appears to be an alternative implementation using a more complex loop, but it is not used in the current implementation.
