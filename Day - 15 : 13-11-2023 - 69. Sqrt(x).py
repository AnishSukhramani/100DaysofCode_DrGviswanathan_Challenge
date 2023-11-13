class Solution(object):
    def mySqrt(self, x):
        if x>=0:
            answer = x**(0.5)
            final_answer = int(answer)
            return final_answer
          
# The code defines a class `Solution` with a method `mySqrt` that calculates the square root of a non-negative integer `x`. If `x` is non-negative, it computes the square root using the exponentiation operator (`**`) and then converts the result to an integer using `int()`. The final integer result is then returned. If `x` is negative, the method does not proceed, and there is no explicit return value for this case, which implies `None` is implicitly returned.
