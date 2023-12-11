class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c=0
        answer=0
        for i in range(len(gain)):
            c+=gain[i]
            if c>=answer:
                answer=c
        return answer
