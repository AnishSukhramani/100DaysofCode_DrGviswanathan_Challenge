class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        elif n<=0 or n%2!=0:
            return False
        else:
            while n>1:
                if n%4!=0:
                    return False
                else:
                    n=n/4
            return True
        
          
# Explanation:

# The method isPowerOfFour takes an integer n as input and returns a boolean (True or False) indicating whether n is a power of 4.
# If n is equal to 1, it directly returns True because 1 is a power of 4 (4^0 = 1).
# If n is less than or equal to 0 or is an odd number (n % 2 != 0), it returns False because powers of 4 are positive integers and are always even.
# The while loop runs as long as n is greater than 1. Inside the loop:
# If n is not divisible by 4 (n % 4 != 0), it means it's not a power of 4, so it returns False.
# If n is divisible by 4, it divides n by 4 (n = n / 4) to check the next power until n becomes 1.
# If the loop completes and n becomes 1, it means that the initial n was a power of 4, so it returns True.
# This function checks whether a number is a power of 4 by continuously dividing it by 4 until the result is 1 (if the number is indeed a power of 4), and it returns False if at any point the number is not divisible by 4.





