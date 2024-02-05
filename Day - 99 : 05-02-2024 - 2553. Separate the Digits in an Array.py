from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            if len(str(i)) > 1:
                for j in str(i):
                    arr.append(int(j))  # Convert each digit to integer before appending
            else:
                arr.append(i)
        return arr
