class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        rev_w=words[::-1]
        result=' '.join(rev_w)
        return result[::-1]
