# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         answer=""
#         for i in indices:
#             answer+=s[i]
#         return answer

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for index, char in enumerate(s):
            res[indices[index]] = char
        return "".join(res)
