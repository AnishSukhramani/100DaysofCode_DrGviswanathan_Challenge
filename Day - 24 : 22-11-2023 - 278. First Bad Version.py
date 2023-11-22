# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
# This Python code implements a solution to find the first occurrence of a "bad version" within a range of versions using a binary search algorithm.
# Here's a breakdown of the code:
      
# 1. The `firstBadVersion` method within the `Solution` class takes an integer `n` as input, representing the total number of versions.
# 2. It uses a binary search algorithm to find the first bad version within the range of versions.
# 3. The binary search is performed within the `while` loop as long as the `left` index is less than the `right` index.
# 4. Inside the loop:
#    - The `mid` variable is calculated as the middle point between `left` and `right`.
#    - If the `isBadVersion(mid)` function returns `True`, indicating that the current version (`mid`) is a bad version:
#        - `right` is updated to `mid` because the bad version might occur before or at the current version.
#    - If `isBadVersion(mid)` returns `False`:
#        - It means the bad version should be after the current version, so `left` is updated to `mid + 1`.
# 5. The loop continues narrowing down the search range until `left` and `right` converge (i.e., `left` becomes equal to `right`). At this point, the loop stops, and the function returns the `left` value, which represents the index of the first bad version.
# 6. The returned `left` value represents the first occurrence of a bad version within the given range of versions.

# Please note:
# - The `isBadVersion` function is assumed to be an external function defined elsewhere that takes a version number as input and returns `True` if the version is bad, and `False` otherwise.
# - The given code uses a binary search strategy to optimize the search for the first bad version within the given range of versions (`1` to `n`).
