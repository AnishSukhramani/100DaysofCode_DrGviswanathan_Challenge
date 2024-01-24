class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        answer=0
        points.sort()
        for i in range(1,len(points)):
            diff=abs((points[i][0])-points[i-1][0])
            if diff>answer:
                answer=diff
        return answer
