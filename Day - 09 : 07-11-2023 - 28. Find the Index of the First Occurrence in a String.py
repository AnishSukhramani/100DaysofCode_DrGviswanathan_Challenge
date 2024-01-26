class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+n]==needle:
                    return i
        else:
            return -1

# The code defines a class `Solution` with a method `strStr` that aims to find the index of the first occurrence of a `needle` string within a `haystack` string. Here's a summary of how it works:
# 1. It calculates the length of the `needle` string and stores it in the variable `n`.
# 2. It checks if the `needle` string is present within the `haystack` string using the `if needle in haystack` condition.
# 3. If the `needle` is found in the `haystack`, it enters a loop to iterate through each character in the `haystack` using the index `i`.
# 4. It checks if a substring of `haystack` starting from index `i` and of length `n` is equal to the `needle` string.
# 5. If a match is found, it returns the index `i`, which represents the starting position of the `needle` in the `haystack`.
# 6. If the `needle` is not found in the `haystack`, it returns -1 to indicate that there is no match.
# However, it's important to note that this code can be optimized by avoiding the unnecessary use of `if needle in haystack` and using a more efficient string comparison approach.
