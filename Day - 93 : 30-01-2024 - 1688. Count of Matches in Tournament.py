class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        while n>1:
            if n%2==0: #even
                n=n/2
                matches+=n
                print("n ",n)
                print(matches)
            else: #odd
                n=(n - 1) / 2 + 1
                matches+=(n - 1) 
                print("n ",n)
                print(matches)
        return int(matches)
