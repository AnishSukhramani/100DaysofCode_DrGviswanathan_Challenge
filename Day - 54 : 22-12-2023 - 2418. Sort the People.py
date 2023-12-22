class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # height_sorted=heights.sort(reverse=True)
        height_sorted=sorted(heights, reverse=True)
        arr=[]
        for i in range(len(height_sorted)):
            # index=heights.index(height_sorted[i])
            arr.append(names[heights.index(height_sorted[i])])
        return arr
