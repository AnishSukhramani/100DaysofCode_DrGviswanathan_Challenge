class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr=s.split(" ")
        answer=""
        for i in range(k-1):
            answer+=arr[i]+" "
        return answer+arr[k-1]
