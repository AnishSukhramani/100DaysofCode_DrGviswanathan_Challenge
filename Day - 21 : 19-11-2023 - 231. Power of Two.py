class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        elif n==0 or n<0:
            return False
        else:
            while n>1:
                if n%2!=0:
                    return False
                else:
                    n=n/2
            return True

# This Python class, `Solution`, contains a method named `isPowerOfTwo`. This method takes an integer `n` as an argument and returns a boolean value (`True` or `False`) based on whether the input integer is a power of two.
# Here's a breakdown of how the method works:
# 1. If the input `n` is equal to `1`, the method returns `True`, as `1` is considered a power of two.
# 2. If the input `n` is `0` or a negative number (`n<0`), the method returns `False`, as neither `0` nor negative numbers are powers of two.
# 3. If the input `n` is a positive integer greater than `1`, the method enters a loop that continues until `n` becomes less than or equal to `1`.
#    - Within the loop, it checks whether `n` is divisible by `2` without leaving a remainder (`n % 2 != 0`). If `n` is not divisible by `2`, it means `n` is not a power of two, so the method returns `False`.
#    - If `n` is divisible by `2`, it updates the value of `n` by dividing it by `2` (`n = n / 2`).
# 4. Once the loop exits (when `n` becomes `1`), the method returns `True`, indicating that the input `n` was indeed a power of two.
# This method employs a straightforward approach to check whether a given number is a power of two by continuously dividing it by `2` until it reaches `1`, checking for remainders in each step. If at any point there's a remainder when dividing by `2`, it concludes that the number is not a power of two and returns `False`. Otherwise, if the loop completes and `n` becomes `1`, the method returns `True`.
