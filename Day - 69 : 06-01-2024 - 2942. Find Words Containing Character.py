class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr=[]
        for i in range(len(words)):
            if x in words[i]:
                arr.append(i)
        return arr
